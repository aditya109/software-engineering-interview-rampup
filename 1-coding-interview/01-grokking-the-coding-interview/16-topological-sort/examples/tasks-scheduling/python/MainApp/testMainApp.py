import unittest

from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'req': [
                    (0, 1),
                    (1, 2)
                ],
                'tasks': 3,
                'expectedResult': True
            },
            {
                'req': [
                    (0, 1),
                    (1, 2),
                    (2, 0)
                ],
                'tasks': 3,
                'expectedResult': False
            },
            {
                'req': [
                    (2, 5),
                    (0, 5),
                    (0, 4),
                    (1, 4),
                    (3, 2),
                    (1, 3)
                ],
                'tasks': 6,
                'expectedResult': True
            },

        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['req'], argument['tasks'])
            self.assertEqual(argument['expectedResult'], actual_result)
