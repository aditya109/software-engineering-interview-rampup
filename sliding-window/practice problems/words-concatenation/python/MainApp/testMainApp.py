from unittest.case import expectedFailure
from app.mainApp import MainApp
import unittest


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'words': ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
                'expectedResult': ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
            },
            {
                'words': ["cat", "dog", "catdog"],
                'expectedResult': ["catdog"]
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actualResult = self._mainAppInstance.run(
                argument['words'])
            self.assertEqual(actualResult, argument['expectedResult'])
