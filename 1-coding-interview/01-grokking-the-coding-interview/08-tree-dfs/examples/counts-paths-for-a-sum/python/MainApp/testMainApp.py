import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()
        start = TreeNode(10)
        start.left = TreeNode(5)
        start.left.left = TreeNode(3)
        start.left.left.left = TreeNode(3)
        start.left.left.right = TreeNode(-2)

        start.left.right = TreeNode(2)
        start.left.right.right = TreeNode(1)

        start.right = TreeNode(-3)
        start.right.right = TreeNode(11)

        self._arguments.append(
            {
                'root': start,
                'targetSum': 8,
                'expectedResult': 3
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'], argument['targetSum'])
            self.assertEqual(argument['expectedResult'], actual_result)
