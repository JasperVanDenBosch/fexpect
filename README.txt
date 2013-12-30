=======
fexpect
=======

Fexpect is an extension to fabric for handling prompts with pexpect scripts.

Provisional documentation in these blogposts:

* http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/
* http://ilogue.com/jasper/blog/improved-fexpect-now-on-pypi/

Please report bugs, request features at the github repository: http://github.com/ilogue/fexpect

Seems it doesn't work well with easy_install, please install with pip.

usage
=====

::

    from ilogue.fexpect import expect, expecting, run

    prompts = []
    prompts += expect('What is your name?','Jasper')
    prompts += expect('Where do you live?','Frankfurt')

    with expecting(prompts):
        run('command')

You can use the included fabfile.py to run the fexpect tests:

::

    fab test -p 'yourlocalpassword'

Note however that the tests may have different requirements (more recent fabric version). You can install these with the traditional:

::

    python setup.py test

contributors
============

* Jasper van den Bosch / ilogue
* Michael Ivanov
* Mitsuhiro Koga
* Erik Dykema

