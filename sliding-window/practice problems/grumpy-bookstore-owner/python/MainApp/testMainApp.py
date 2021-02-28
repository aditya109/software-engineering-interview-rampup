from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's': "abciiidef",
                'k': 3,
                'expectedResult': 3
            },
            {
                's': "aeiou",
                'k': 2,
                'expectedResult': 2
            },
            {
                's': "leetcode",
                'k': 3,
                'expectedResult': 2
            },
            {
                's': "rhythms",
                'k': 4,
                'expectedResult': 0
            },
            {
                's': "tryhard",
                'k': 4,
                'expectedResult': 1
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
