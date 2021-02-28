from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's': "ABAB",
                'k': 2,
                'expectedResult': 4
            },
            {
                's': "AABABBA",
                'k': 1,
                'expectedResult': 4
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['s'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
