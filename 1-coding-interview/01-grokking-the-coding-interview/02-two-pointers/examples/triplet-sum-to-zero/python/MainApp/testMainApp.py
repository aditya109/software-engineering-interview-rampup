from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'nums': [-1, 0, 1, 2, -1, -4],
                'expectedResult': [[-1, -1, 2], [-1, 0, 1]]
            },
            {
                'nums': [],
                'expectedResult': []
            },
            {
                'nums': [0],
                'expectedResult': []
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['nums'])
            self.assertEqual(actualResult, argument['expectedResult'])
