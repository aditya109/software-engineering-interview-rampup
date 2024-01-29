import unittest

from app.mainApp import MainApp, ListNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = [
            {
                'head': ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
                'expectedResult': ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
            },
            {
                'head': ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
                'expectedResult': ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
            },
        ]
        self._mainAppInstance = MainApp()

    def test_run(self):
        def check_if_equal(list1, list2):
            while list1:
                if list1.val != list2.val:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True

        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['head'])
            self.assertTrue(check_if_equal(argument['expectedResult'], actual_result))
