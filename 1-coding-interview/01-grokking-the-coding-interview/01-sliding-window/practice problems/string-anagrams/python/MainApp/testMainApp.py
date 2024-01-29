from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's': "cbaebabacd",
                'p': "abc",
                'expectedResult': [0, 6]
            },
            {
                's': "abab",
                'p': "ab",
                'expectedResult': [0, 1, 2]
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['s'], argument['p'])
            self.assertEqual(actualResult, argument['expectedResult'])
