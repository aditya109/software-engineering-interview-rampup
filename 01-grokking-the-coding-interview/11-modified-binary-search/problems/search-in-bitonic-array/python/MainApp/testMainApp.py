import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 3,
                'expectedResult': 16
            },
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 4,
                'expectedResult': 19
            },
            {
                'arr': [4, 2, 1, 7, 8, 1, 2, 8, 1, 0],
                'k': 5,
                'expectedResult': 26
            },
            {
                'arr': [4, 2, 1, 7, 8, 8, 1, 0],
                'k': 3,
                'expectedResult': 23
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['arr'])
            self.assertEqual(argument['expectedResult'], actual_result)
