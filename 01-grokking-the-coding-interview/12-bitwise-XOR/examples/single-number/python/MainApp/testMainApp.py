import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [2, 2, 1],
                'expectedResult': 1
            },
            {
                'arr': [4, 1, 2, 1, 2],
                'expectedResult': 4
            },
            {
                'arr': [1],
                'expectedResult': 1
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['arr'])
            self.assertEqual(argument['expectedResult'], actual_result)
