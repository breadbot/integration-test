import os
import time

import unittest

class Test(unittest.TestCase):
    def test_fail(self):
        print "BUILD_NUMBER(%s)" % (os.environ['BUILD_NUMBER'])
	self.fail()
        pass
