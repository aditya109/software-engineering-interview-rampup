from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [-4, -1, 0, 3, 10],
                'expectedResult': [0, 1, 9, 16, 100]
            },

            {
                'arr': [-7, -3, 2, 3, 11],
                'expectedResult': [4, 9, 9, 49, 121]
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'])
            self.assertEqual(actualResult, argument['expectedResult'])
