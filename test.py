import os
import time

import unittest

class Test(unittest.TestCase):
    def test_fail_on_even_builds(self):
	if int(os.environ['BUILD_NUMBER']) % 2 == 0:
	    self.fail()
        else:
            pass
