fexpect

Fexpect is an extension to fabric for handling prompts with pexpect scripts.

Original blogpost:
http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/

COPYRIGHT / LICENSE

Pexpect Copyright (c) 2012 Noah Spurrier, see: http://www.noah.org/wiki/pexpect
this package Copyright (c) Jasper van den Bosch, ilogue, jasper@ilogue.com

USAGE

from ilogue.fexpect import expect, expecting, run

prompts = []
prompts += expect(‘What is your name?’,'Jasper')
prompts += expect('Where do you live?','Frankfurt')

with expecting(prompts):
    run(‘command’)

#tests:

# Run from a fabfile.py with:
@task()
def test():
    from ilogue.tests import FexpectTests, runtest
    runtest(FexpectTests)

CONTRIBUTORS

Jasper van den Bosch - ilogue
Michael Ivanov


