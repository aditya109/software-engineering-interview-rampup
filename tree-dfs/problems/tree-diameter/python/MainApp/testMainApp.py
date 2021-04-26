import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        start = TreeNode(1)
        start.left = TreeNode(2)
        start.left.left = TreeNode(4)
        start.left.right = TreeNode(5)
        start.right = TreeNode(3)
        self._arguments = [
            {
                'root': start,
                'expectedResult': 3
            }
        ]
        start = TreeNode(1)
        start.left = TreeNode(2)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': 1
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertEqual(argument['expectedResult'], actual_result)
