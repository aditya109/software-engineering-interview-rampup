from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [1, 1, 2],
                'expectedResult1': 2,
                'expectedResult2': [1, 2],
            },
            {
                'arr': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
                'expectedResult1': 5,
                'expectedResult2':[0, 1, 2, 3, 4],
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'])
            self.assertEqual(
                actualResult, (argument['expectedResult1'], argument['expectedResult2']))
