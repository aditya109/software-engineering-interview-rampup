import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'graph': {
                    'A': ['D'],
                    'B': ['D'],
                    'C': ['E'],
                    'D': ['E'],
                    'E': []
                },
                'start': 'A',
                'expectedResult': ['C', 'B', 'A', 'D', 'E']
            },
            {
                'graph': {
                    '0': [],
                    '1': [],
                    '2': ['3'],
                    '3': ['1'],
                    '4': ['0', '1'],
                    '5': ['0', '2']
                },
                'start': 'A',
                'expectedResult': ['5', '4', '2', '3', '1', '0']
            }
        ]

        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['graph'], argument['start'])
            self.assertEqual(argument['expectedResult'], actual_result)
