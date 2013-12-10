import unittest
import sys
from fabric.api import *


def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fexpect test wrapper] One or more tests failed!')

class FexpectTests(unittest.TestCase):

    def test_one_expectation(self):
        cmd = 'echo "Hello" && read NAME && echo "Hi $NAME."'
        from ilogue.fexpect import expect, expecting, run
        expectation =  expect('Hello','answer')
        with expecting(expectation):
            output = run(cmd)
        self.assertIn('answer',output)

    def test_two_expectations(self):
        cmd = 'echo "Hello" && read ONE && echo "bladiebla" && read TWO && echo "First $ONE than $TWO."'
        from ilogue.fexpect import expect, expecting, run
        exp1 =  expect('Hello','111')
        exp2 =  expect('bladiebla','222')
        with expecting(exp1+exp2):
            output = run(cmd)
        self.assertIn('111',output)
        self.assertIn('222',output)

    def test_order_inconsequential(self):
        #sequence shouldn't matter
        cmd = 'echo "Hello" && read ONE && echo "bladiebla" && read TWO && echo "First $ONE than $TWO."'
        from ilogue.fexpect import expect, expecting, run
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
        from ilogue.fexpect import expect, expecting, run
        exp1 =  expect('Hello','111')
        exp2 =  expect('3','expected',exitAfter=0)
        t = time.time()
        with expecting(exp1+exp2):
            output = run(cmd)
        elapsed = time.time() - t
        self.assertGreater(elapsed,2)
        self.assertLess(elapsed,4)

    def test_one_expectation_local(self):
        cmd = 'echo "Hello" && read NAME && echo "Hi $NAME."'
        from ilogue.fexpect import expect, expecting, local
        expectation =  expect('Hello','answer')
        with expecting(expectation):
            output = local(cmd,capture=True)
        self.assertIn('answer',output)

    def test_can_change_shell(self):
        cmd = 'ps c && echo "Hello" && read NAME && echo "Hi $NAME."'
        from ilogue.fexpect import expect, expecting, run
        import fabric
        expectation =  expect('Hello','answer')
        backupenv = dict(fabric.state.env)
        fabric.state.env.shell = 'sh -c'
        with expecting(expectation):
            output = run(cmd)
        fabric.state.env.update(backupenv)
        self.assertIn('00 sh',output)

    def test_mixed_case(self):
        cmd1 = 'expr 5 + 5'
        cmd2 = 'read -p Name: NAME && echo Hi $NAME.'
        cmd3 = 'expr 18 / 3'

        from ilogue.fexpect import expect, expecting, run
        import fabric

        output1 = run(cmd1)
        expectation =  expect('Name:','Bill')
        with expecting(expectation):
            output2 = run(cmd2)
        output3 = run(cmd3)

        self.assertIn('10',output1)
        self.assertIn('Hi Bill.',output2)
        self.assertIn('6',output3)

    def test_quotes(self):
        cmd1 = 'read -p "Prompt1:" RESP1 && echo Received $RESP1.'
        cmd2 = "read -p 'Prompt2:' RESP2 && echo Received $RESP2."
        cmd3 = """read -p 'Prompt3:' -n "20" RESP3 && echo Received $RESP3."""

        from ilogue.fexpect import expect, expecting, run
        import fabric

        expectation =  []
        expectation += expect('Prompt1:','Foo')
        expectation += expect('Prompt2:','Bar')
        expectation += expect('Prompt3:','Baz')

        with expecting(expectation):
            output1 = run(cmd1)
            output2 = run(cmd2)
            output3 = run(cmd3)

        self.assertIn('Received Foo',output1)
        self.assertIn('Received Bar',output2)
        self.assertIn('Received Baz',output3)

    def tryOrFailOnPrompt(self,method,args):
        try:
            with settings(abort_on_prompts=True):
                result = method(*args)
        except SystemExit as promptAbort:
            self.fail("There was an unexpected (password) prompt.")
        return result 
