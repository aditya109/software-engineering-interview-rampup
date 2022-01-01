import unittest

from app.mainApp import MainApp, ListNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()

        node_1a = ListNode(1)
        node_2a = ListNode(2)
        node_2b = ListNode(2)
        node_1b = ListNode(1)

        node_1a.next = node_2a
        node_2a.next = node_2b
        node_2b.next = node_1b

        self._arguments.append(
            {
                'head': node_1a,
                'expectedResult': True
            }
        )

        node_1a = ListNode(1)
        node_2a = ListNode(2)
        node_1b = ListNode(1)

        node_1a.next = node_2a
        node_2a.next = node_1b

        self._arguments.append(
            {
                'head': node_1a,
                'expectedResult': True
            }
        )

        node_1a = ListNode(1)
        node_2a = ListNode(2)

        node_1a.next = node_2a

        self._arguments.append(
            {
                'head': node_1a,
                'expectedResult': False
            }
        )

        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['head'])
            self.assertEqual(argument['expectedResult'], actual_result)
