from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'nums': [2, 7, 11, 15],
                'target': 9,
                'expectedResult': [0, 1]
            },

            {
                'nums': [2, 3, 4],
                'target': 6,
                'expectedResult': [0, 2]
            },

            {
                'nums': [3, 3],
                'target': 6,
                'expectedResult': [0, 1]
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['nums'], argument['target'])
            self.assertEqual(actualResult, argument['expectedResult'])
