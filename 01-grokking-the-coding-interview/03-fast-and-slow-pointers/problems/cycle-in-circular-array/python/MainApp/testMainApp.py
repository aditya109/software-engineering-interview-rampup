import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [2, -1, 1, 2, 2],
                'expectedResult': True
            },
            {
                'arr': [-1, 2],
                'expectedResult': False
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['arr'])
            self.assertEqual(argument['expectedResult'], actual_result)
