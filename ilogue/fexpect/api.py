import fabric.api
from ilogue.fexpect.internals import wrapExpectations, ExpectationContext


def expect(promptexpr, response, exitAfter=-1):
    if not exitAfter == -1:
        return [(promptexpr, response, exitAfter)]
    return [(promptexpr, response)]

def expecting(e):
    return ExpectationContext(e)

def run(cmd):
    #run wrapper
    wrappedCmd = wrapExpectations(cmd)
    return fabric.api.run(wrappedCmd)

def sudo(cmd):
    #sudo wrapper
    wrappedCmd = wrapExpectations(cmd)
    return fabric.api.sudo(wrappedCmd)

