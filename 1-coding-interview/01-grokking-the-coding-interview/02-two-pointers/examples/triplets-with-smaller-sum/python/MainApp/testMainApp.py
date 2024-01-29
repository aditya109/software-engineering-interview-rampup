from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [-2, 0, 1, 3],
                'k': 2,
                'expectedResult': 2
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['arr'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
