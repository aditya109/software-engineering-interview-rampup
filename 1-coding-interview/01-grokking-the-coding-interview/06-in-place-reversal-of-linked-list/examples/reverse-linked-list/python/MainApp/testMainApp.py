import unittest

from app.mainApp import MainApp, ListNode


def is_equal(a, b):
    while a and b:
        if a.val != b.val:
            return False
        a = a.next
        b = b.next
    return True


class TestMainApp(unittest.TestCase):

    def setUp(self):
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)

        r_root = ListNode(5)
        r_root.next = ListNode(4)
        r_root.next.next = ListNode(3)
        r_root.next.next.next = ListNode(2)
        r_root.next.next.next.next = ListNode(1)

        self._arguments = [
            {
                'head': root,
                'expectedResult': r_root
            }
        ]
        root = ListNode(1)
        root.next = ListNode(2)

        r_root = ListNode(2)
        r_root.next = ListNode(1)
        self._arguments.append({
            'head': root,
            'expectedResult': r_root
        })
        root = None
        r_root = None

        self._arguments.append({
            'head': root,
            'expectedResult': r_root
        })
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['head'])
            self.assertTrue(is_equal(argument['expectedResult'], actual_result))
