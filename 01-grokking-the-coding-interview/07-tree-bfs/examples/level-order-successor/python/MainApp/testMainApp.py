import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self._arguments = list()
        start = TreeNode(2)
        start.right = TreeNode(3)
        start.right.right = TreeNode(4)
        start.right.right.right = TreeNode(5)
        start.right.right.right.right = TreeNode(5)
        self._arguments.append(
            {
                'root': start,
                'key': 4,
                'expectedResult': start.right.right.right
            }
        )

        start = TreeNode(3)
        start.left = TreeNode(9)
        start.right = TreeNode(20)

        start.right.left = TreeNode(15)
        start.right.right = TreeNode(7)
        self._arguments.append(
            {
                'root': start,
                'key': 15,
                'expectedResult': start.right.right
            }
        )
        start = TreeNode(1)
        self._arguments.append(
            {
                'root': start,
                'key': 1,
                'expectedResult': None
            }
        )

        start = TreeNode(20)
        start.left = TreeNode(10)
        start.left.left = TreeNode(4)
        start.left.right = TreeNode(18)
        start.left.right.left = TreeNode(14)
        start.left.right.left.left = TreeNode(13)
        start.left.right.left.right = TreeNode(15)

        start.left.right.right = TreeNode(19)

        start.right = TreeNode(26)
        start.right.left = TreeNode(24)
        start.right.right = TreeNode(27)
        self._arguments.append(
            {
                'root': start,
                'key': 24,
                'expectedResult': start.right.right
            }
        )
        self._arguments.append(
            {
                'root': start,
                'key': 4,
                'expectedResult': start.left.right
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'], argument['key'])
            self.assertEqual(argument['expectedResult'], actual_result)
