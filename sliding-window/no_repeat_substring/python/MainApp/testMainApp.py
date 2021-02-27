from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's': "abcabcbb",
                'expectedResult': 3
            },
            {
                's': "bbbbb",
                'expectedResult': 1
            },
            {
                's': "pwwkew",
                'expectedResult': 3
            },
            {
                's': "",
                'expectedResult': 0
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['s'])
            self.assertEqual(actualResult, argument['expectedResult'])
