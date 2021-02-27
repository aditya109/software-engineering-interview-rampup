from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
                'k': 2,
                'expectedResult': 6
            },
            {
                'arr': [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                'k': 3,
                'expectedResult': 10
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
