import fabric.api
from ilogue.fexpect.internals import wrapExpectations, wrapExpectationsLocal, ExpectationContext


def expect(promptexpr, response, exitAfter=-1):
    if not exitAfter == -1:
        return [(promptexpr, response, exitAfter)]
    return [(promptexpr, response)]

# Use inside an expect(), like:  `expect('>>>', controlchar('D'))`
def controlchar(char):
    char = char.lower()
    a = ord(char)
    if a >= 97 and a <= 122:
        a = a - ord('a') + 1
        return chr(a)
    d = {'@': 0, '`': 0,
        '[': 27, '{': 27,
        '\\': 28, '|': 28,
        ']': 29, '}': 29,
        '^': 30, '~': 30,
        '_': 31,
        '?': 127}
    if char not in d:
        return 0
    return chr(d[char])

def expecting(e, show_response=True):
    return ExpectationContext(e, show_response)

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

