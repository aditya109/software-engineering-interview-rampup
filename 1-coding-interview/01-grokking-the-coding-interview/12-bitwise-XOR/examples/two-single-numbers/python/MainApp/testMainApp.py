import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [2, 2, 3, 2],
                'expectedResult': 3
            },
            {
                'arr': [0, 1, 0, 1, 0, 1, 99],
                'expectedResult': 99
            }
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['arr'])
            self.assertEqual(argument['expectedResult'], actual_result)
