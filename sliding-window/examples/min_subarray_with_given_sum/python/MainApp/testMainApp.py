from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [2, 3, 1, 2, 4, 3],
                'target_sum': 7,
                'expectedResult': 2
            },
            {
                'arr': [1, 4, 4],
                'target_sum': 4,
                'expectedResult': 1
            },
            {
                'arr': [1, 1, 1, 1, 1, 1, 1, 1],
                'target_sum': 11,
                'expectedResult': 0
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'], argument['target_sum'])
            self.assertEqual(actualResult, argument['expectedResult'])
