import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'arr': [[1, 3], [2, 6], [8, 10], [15, 18]],
                'expectedResult': [[1, 6], [8, 10], [15, 18]]
            },
            {
                'arr': [[1, 4], [4, 5]],
                'expectedResult': [[1, 5]]
            },
            {
                'arr': [[1, 4]],
                'expectedResult': [[1, 4]]
            },
            {
                'arr': [[1, 4], [5, 6]],
                'expectedResult': [[1, 4], [5, 6]]
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['arr'])
            self.assertEqual(argument['expectedResult'], actual_result)
