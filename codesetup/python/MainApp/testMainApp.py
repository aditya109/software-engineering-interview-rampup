from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 3,
                'expectedResult': 16
            },
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 4,
                'expectedResult': 19
            },
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 5,
                'expectedResult': 26
            },
            {
                'arr': [4, 2, 1, 7, 8, 8, 1, 0],
                'k': 3,
                'expectedResult': 23
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(argument['arr'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])