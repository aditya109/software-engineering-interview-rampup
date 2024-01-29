from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's': "eceba",
                'k': 3,
                'expectedResult': 4
            },
            {
                's': "WORLD",
                'k': 4,
                'expectedResult': 4
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['s'], argument['k'])
            self.assertEqual(actualResult, argument['expectedResult'])
