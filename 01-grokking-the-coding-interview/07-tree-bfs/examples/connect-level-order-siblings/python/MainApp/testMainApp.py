import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()
        start = TreeNode(3)
        start.left = TreeNode(9)
        start.right = TreeNode(20)

        start.left.left = TreeNode(15)
        start.left.right = TreeNode(7)

        expected_start = start
        expected_start.left.next = expected_start.right
        expected_start.left.left.next = expected_start.left.right
        self._arguments.append(
            {
                'root': start,
                'expectedResult': expected_start
            }
        )

        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)

        start.left.left = TreeNode(4)
        start.left.right = TreeNode(5)
        start.right.left = TreeNode(6)
        start.right.right = TreeNode(7)

        expected_start = start
        expected_start.left.next = expected_start.right
        expected_start.left.left.next = expected_start.left.right
        expected_start.left.right.next = expected_start.right.left
        expected_start.right.left.next = expected_start.right.right
        self._arguments.append(
            {
                'root': start,
                'expectedResult': expected_start
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertTrue(argument['expectedResult'], actual_result)
