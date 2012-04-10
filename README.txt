=======
fexpect
=======

Fexpect is an extension to fabric for handling prompts with pexpect scripts.

Provisional documentation in these blogposts:

* http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/
* http://ilogue.com/jasper/blog/improved-fexpect-now-on-pypi/

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

contributors
============

* Jasper van den Bosch - ilogue
* Michael Ivanov

