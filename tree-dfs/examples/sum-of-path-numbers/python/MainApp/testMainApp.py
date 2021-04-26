import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)
        self._arguments = [
            {
                'root': start,
                'expectedResult': 25
            }
        ]
        start = TreeNode(4)
        start.left = TreeNode(9)
        start.left.left = TreeNode(5)
        start.left.right = TreeNode(1)
        start.right = TreeNode(0)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': 1026
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertEqual(argument['expectedResult'], actual_result)
