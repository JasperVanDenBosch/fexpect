fexpect

Fexpect is an extension to fabric for handling prompts with pexpect scripts.

blogpostz:
http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/
http://ilogue.com/jasper/blog/improved-fexpect-now-on-pypi/

COPYRIGHT / LICENSE

Pexpect Copyright (c) 2012 Noah Spurrier, see: http://www.noah.org/wiki/pexpect
this package Copyright (c) Jasper van den Bosch, ilogue, jasper@ilogue.com
(still thinking about license, feedback welcome)

USAGE

from ilogue.fexpect import expect, expecting, run

prompts = []
prompts += expect('What is your name?','Jasper')
prompts += expect('Where do you live?','Frankfurt')

with expecting(prompts):
    run('command')

# You can use the included fabfile.py to run the fexpect tests:
fab test -p 'yourlocalpassword'

CONTRIBUTORS

Jasper van den Bosch - ilogue
Michael Ivanov


