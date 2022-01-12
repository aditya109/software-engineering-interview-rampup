import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'k': 5,
                'expectedResult': 2
            },
            {
                'k': 7,
                'expectedResult': 0
            },
            {
                'k': 10,
                'expectedResult': 5
            }
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['k'])
            self.assertEqual(argument['expectedResult'], actual_result)
