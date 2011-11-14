import os
import time

import unittest

class Test(unittest.TestCase):
    def test_fail(self):
	print os.getcwd()
        self.fail()
        pass
