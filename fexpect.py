# fabric extension to enable handling expected prompts
#
# Read more at http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/
#
# This file Copyright (c) Jasper van den Bosch, ilogue, jasper@ilogue.com
# Pexpect Copyright (c) 2012 Noah Spurrier ,see: http://www.noah.org/wiki/pexpect#License


from fabric.state import env
import fabric.api
import shortuuid
from general import resource
from StringIO import StringIO

def expect(promptexpr, response, exitAfter=-1):
    if not exitAfter == -1:
        return [(promptexpr, response, exitAfter)]
    return [(promptexpr, response)]

def expecting(e):
    return ExpectationContext(e)

class ExpectationContext(object):
    def __init__(self,expectations):
        self.expectations = expectations
    def __enter__(self):
        env.expectations = self.expectations
    def __exit__(self, type, value, tb):
        env.expectations = []

def run(cmd):
    #sudo wrapper
    wrappedCmd = wrapExpectations(cmd,env)
    return fabric.api.run(wrappedCmd)

def sudo(cmd):
    #sudo wrapper
    wrappedCmd = wrapExpectations(cmd,env)
    return fabric.api.sudo(wrappedCmd)

def wrapExpectations(cmd,env):
    script = createScript(cmd,env)
    remoteScript = '/tmp/fexpect_'+shortuuid.uuid()
    fabric.api.put(resource('pexpect.py'),'/tmp/')
    fabric.api.put(StringIO(script),remoteScript)
    wrappedCmd = 'python '+remoteScript
    return wrappedCmd

def createScript(cmd,env):
    to = 30*60 # readline timeout 8 hours
    #write header:
    s = '#!/usr/bin/python\n'
    s+= 'import sys\n'
    s+= 'from time import sleep\n'
    s+= 'import pexpect\n'
    #write expectation list:
    s+= 'expectations=['
    for e in env.expectations:
        s+= '"{0}",'.format(e[0])
    s+= ']\n'
    #start
    s+= """child = pexpect.spawn('/bin/bash -c "{0}"',timeout={1})\n""".format(cmd,to)
    s+= "child.logfile = sys.stdout\n"
    s+= "while True:\n"
    s+= "\ttry:\n"
    s+= "\t\ti = child.expect(expectations)\n"
    i = 0
    for e in env.expectations:
        ifkeyw = 'if' if i == 0 else 'elif'
        s+= "\t\t{0} i == {1}:\n".format(ifkeyw,i)
        s+= "\t\t\tchild.sendline('{0}')\n".format(e[1])
        if len(e)>2:
            s+= "\t\t\tsleep({0})\n".format(e[2])
            s+= "\t\t\tprint('Exiting fexpect for expected exit.')\n"
            s+= '\t\t\tbreak\n'
        i += 1
    s+= '\texcept pexpect.EOF:\n'
    s+= "\t\tprint('Exiting fexpect for EOF.')\n"
    s+= '\t\tbreak\n'
    s+= '\n'
    return s
