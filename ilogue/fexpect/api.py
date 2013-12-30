import fabric.api
from ilogue.fexpect.internals import wrapExpectations, wrapExpectationsLocal, ExpectationContext


def expect(promptexpr, response, exitAfter=-1):
    if not exitAfter == -1:
        return [(promptexpr, response, exitAfter)]
    return [(promptexpr, response)]

def expecting(e):
    return ExpectationContext(e)

def run(cmd, **kwargs):
    #run wrapper 
    if 'expectations' in fabric.state.env and \
        len(fabric.state.env.expectations) > 0:
        cmd = wrapExpectations(cmd)
    return fabric.api.run(cmd, **kwargs)

def sudo(cmd, **kwargs):
    #sudo wrapper
    if 'expectations' in fabric.state.env and \
        len(fabric.state.env.expectations) > 0:
        cmd = wrapExpectations(cmd)
    return fabric.api.sudo(cmd, **kwargs)

def local(cmd, **kwargs):
    #local wrapper
    if 'expectations' in fabric.state.env and \
        len(fabric.state.env.expectations) > 0:
        cmd = wrapExpectationsLocal(cmd)
    return fabric.api.local(cmd, **kwargs)

