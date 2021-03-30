from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [2, 6, 4, 8, 10, 9, 15],
                'expectedResult': 5
            },
            {
                'arr': [1, 2, 3, 4],
                'expectedResult': 0
            },
            {
                'arr': [1],
                'expectedResult': 0
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'])
            self.assertEqual(actualResult, argument['expectedResult'])
