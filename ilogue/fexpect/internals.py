import shortuuid
from StringIO import StringIO
import fabric


class ExpectationContext(object):
    def __init__(self,expectations):
        self.expectations = expectations
    def __enter__(self):
        fabric.state.env.expectations = self.expectations
    def __exit__(self, type, value, tb):
        fabric.state.env.expectations = []

def wrapExpectations(cmd):
    script = createScript(cmd)
    remoteScript = '/tmp/fexpect_'+shortuuid.uuid()
    import pexpect
    pexpect_module = pexpect.__file__
    if pexpect_module.endswith('.pyc'):
        pexpect_module = pexpect_module[:-1]
    fabric.api.put(pexpect_module,'/tmp/')
    fabric.api.put(StringIO(script),remoteScript)
    wrappedCmd = 'python '+remoteScript
    return wrappedCmd

def createScript(cmd):
    useShell =fabric.state.env.shell
    to = 30*60 # readline timeout 8 hours
    #write header:
    s = '#!/usr/bin/python\n'
    s+= 'import sys\n'
    s+= 'from time import sleep\n'
    s+= 'import pexpect\n'
    #write expectation list:
    s+= 'expectations=['
    for e in fabric.state.env.expectations:
        s+= '"{0}",'.format(e[0])
    s+= ']\n'
    #start
    spwnTem = """child = pexpect.spawn('/bin/{shell} "{cmd}"',timeout={to})\n"""
    s+= spwnTem.format(shell=useShell,cmd=cmd,to=to)
    s+= "child.logfile = sys.stdout\n"
    s+= "while True:\n"
    s+= "\ttry:\n"
    s+= "\t\ti = child.expect(expectations)\n"
    i = 0
    for e in fabric.state.env.expectations:
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
