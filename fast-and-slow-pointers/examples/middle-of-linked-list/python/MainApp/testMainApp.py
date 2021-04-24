import unittest

from app.mainApp import MainApp, ListNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._mainAppInstance = MainApp()

        self._arguments = [
            {
                'head': ListNode(1,
                                 ListNode(2,
                                          ListNode(3,
                                                   ListNode(4,
                                                            ListNode(5, None))))),
                'expectedResult': 3
            },
            {
                'head': ListNode(1,
                                 ListNode(2,
                                          ListNode(3,
                                                   ListNode(4,
                                                            ListNode(5,
                                                                     ListNode(6, None)))))),
                'expectedResult': 4
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['head'])
            self.assertEqual(argument['expectedResult'], actual_result)
