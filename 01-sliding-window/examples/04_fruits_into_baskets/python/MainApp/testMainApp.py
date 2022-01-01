from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [1, 2, 1],
                'expectedResult': 3
            },
            {
                'arr':  [0, 1, 2, 2],
                'expectedResult': 3
            },
            {
                'arr': [1, 2, 3, 2, 2],
                'expectedResult': 4
            },
            {
                'arr': [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4],
                'expectedResult': 5
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'])
            self.assertEqual(actualResult, argument['expectedResult'])
