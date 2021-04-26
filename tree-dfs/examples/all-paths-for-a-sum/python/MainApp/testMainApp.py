import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        start = TreeNode(5)
        start.left = TreeNode(4)
        start.left.left = TreeNode(11)
        start.left.left.left = TreeNode(7)
        start.left.left.right = TreeNode(2)

        start.right = TreeNode(8)
        start.right.left = TreeNode(13)
        start.right.right = TreeNode(4)
        start.right.right.left = TreeNode(5)
        start.right.right.right = TreeNode(1)
        self._arguments = [
            {
                'root': start,
                'targetSum': 22,
                'expectedResult': [[5, 4, 11, 2], [5, 8, 4, 5]]
            }
        ]
        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)
        self._arguments.append(
            {
                'root': start,
                'targetSum': 5,
                'expectedResult': []
            }
        )
        start = TreeNode(1)
        start.left = TreeNode(2)
        self._arguments.append(
            {
                'root': start,
                'targetSum': 0,
                'expectedResult': []
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'], argument['targetSum'])
            self.assertEqual(argument['expectedResult'], actual_result)
