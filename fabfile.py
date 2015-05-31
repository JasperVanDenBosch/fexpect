# Example fabfile to run fexpect tests.
#
# run e.g.: fab test -p yourlocalpassword
from fabric.api import *
from ilogue.fexpect.tests import FexpectTests, runtest

env.hosts = ['localhost']

@task()
def test():
    runtest(FexpectTests)
