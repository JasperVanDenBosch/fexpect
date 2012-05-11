import fabric.api
from ilogue.fexpect.internals import wrapExpectations, ExpectationContext


def expect(promptexpr, response, exitAfter=-1):
    if not exitAfter == -1:
        return [(promptexpr, response, exitAfter)]
    return [(promptexpr, response)]

def expecting(e):
    return ExpectationContext(e)

def run(cmd, **kwargs):
    #run wrapper
    wrappedCmd = wrapExpectations(cmd)
    return fabric.api.run(wrappedCmd, **kwargs)

def sudo(cmd, **kwargs):
    #sudo wrapper
    wrappedCmd = wrapExpectations(cmd)
    return fabric.api.sudo(wrappedCmd, **kwargs)

def local(cmd, **kwargs):
    #local wrapper
    wrappedCmd = wrapExpectations(cmd)
    return fabric.api.local(wrappedCmd, **kwargs)

