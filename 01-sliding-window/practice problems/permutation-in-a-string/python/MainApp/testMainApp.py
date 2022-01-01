from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                's1': "ab",
                's2': "eidbaooo",
                'expectedResult': True
            },
            {
                's1': "ab",
                's2': "eidooo",
                'expectedResult': False
            },
            {
                's1': "ab",
                's2': "eidbbooo",
                'expectedResult': False
            },
            {
                's1': "ab",
                's2': "eidabbooo",
                'expectedResult': True
            },
            {
                's1': "ab",
                's2': "",
                'expectedResult': False
            },
            {
                's1': "",
                's2': "",
                'expectedResult': True
            },
            {
                's1': "",
                's2': "ab",
                'expectedResult': True
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['s1'], argument['s2'])
            self.assertEqual(actualResult, argument['expectedResult'])
