# fabric extension to enable handling expected prompts
#
# Read more at http://ilogue.com/jasper/blog/fexpect--dealing-with-prompts-in-fabric-with-pexpect/
#
# This file Copyright (c) Jasper van den Bosch, ilogue, jasper@ilogue.com
# Pexpect Copyright (c) 2012 Noah Spurrier ,see: http://www.noah.org/wiki/pexpect#License

# Run from a fabfile.py with:
#@task()
#def test():
#    from tests import FexpectTests, runtest
#    runtest(FexpectTests)

import unittest
from fabric.api import *

def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    unittest.TextTestRunner(verbosity=2).run(suite)

class FexpectTests(unittest.TestCase):

    def test_one_expectation(self):
        cmd = 'echo "Hello" && read NAME && echo "Hi $NAME."'
        from fexpect import expect, expecting, run
        expectation =  expect('Hello','answer')
        with expecting(expectation):
            output = run(cmd)
        self.assertIn('answer',output)

    def test_two_expectations(self):
        cmd = 'echo "Hello" && read ONE && echo "bladiebla" && read TWO && echo "First $ONE than $TWO."'
        from fexpect import expect, expecting, run
        exp1 =  expect('Hello','111')
        exp2 =  expect('bladiebla','222')
        with expecting(exp1+exp2):
            output = run(cmd)
        self.assertIn('111',output)
        self.assertIn('222',output)

    def test_order_inconsequential(self):
        #sequence shouldn't matter
        cmd = 'echo "Hello" && read ONE && echo "bladiebla" && read TWO && echo "First $ONE than $TWO."'
        from fexpect import expect, expecting, run
        exp1 =  expect('Hello','111')
        exp2 =  expect('bladiebla','222')
        with expecting(exp2+exp1):
            output = run(cmd)
        self.assertIn('111',output)
        self.assertIn('222',output)

    def test_exit_after_expectation(self):
        import time
        from StringIO import StringIO
        #sequence shouldn't matter
        script = "#!/usr/bin/python\nimport time\nfor i in range(1,8):\n\tprint(i)\n\ttime.sleep(1)"
        cmd = 'python /tmp/test.py'
        put(StringIO(script),'/tmp/test.py')
        from fexpect import expect, expecting, run
        exp1 =  expect('Hello','111')
        exp2 =  expect('3','expected',exitAfter=0)
        t = time.time()
        with expecting(exp1+exp2):
            output = run(cmd)
        elapsed = time.time() - t
        self.assertGreater(elapsed,2)
        self.assertLess(elapsed,4)

    def tryOrFailOnPrompt(self,method,args):
        try:
            with settings(abort_on_prompts=True):
                result = method(*args)
        except SystemExit as promptAbort:
            self.fail("There was an unexpected (password) prompt.")
        return result 