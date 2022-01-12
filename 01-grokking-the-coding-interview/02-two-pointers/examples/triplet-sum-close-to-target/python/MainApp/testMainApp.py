from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'nums': [-1, 2, 1, -4],
                'target': 1,
                'expectedResult': 2
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['nums'], argument['target'])
            self.assertEqual(actualResult, argument['expectedResult'])
