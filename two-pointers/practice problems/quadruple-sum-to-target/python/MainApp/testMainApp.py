from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [1, 0, -1, 0, -2, 2],
                'k': 0,
                'expectedResult': [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
            },
            {
                'arr': [],
                'k': 0,
                'expectedResult': []
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
