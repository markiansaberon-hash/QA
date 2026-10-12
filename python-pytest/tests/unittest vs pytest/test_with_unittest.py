import unittest
from unittest import TestCase

class TryTesting(TestCase): 
    def test_always_passes(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_always_fails(self):
        self.assertTrue(False)