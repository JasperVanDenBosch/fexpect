# Example fabfile to run fexpect tests.
#
# run e.g.: fab test -p yourlocalpassword
from fabric.api import *

env.hosts = ['localhost']

@task()
def test():
    from ilogue.fexpect.tests import FexpectTests, runtest
    runtest(FexpectTests)
