import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()
        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)
        start.left.right = TreeNode(5)
        start.right.right = TreeNode(4)
        self._arguments.append({
            'root': start,
            'expectedResult': [1, 3, 4]
        })

        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)
        start.left.right = TreeNode(5)
        start.left.right.right = TreeNode(7)
        start.right.right = TreeNode(4)
        self._arguments.append({
            'root': start,
            'expectedResult': [1, 3, 4, 7]
        })

        start = TreeNode(1)
        start.right = TreeNode(3)
        self._arguments.append({
            'root': start,
            'expectedResult': [1, 3]
        })

        start = TreeNode(1)
        self._arguments.append({
            'root': start,
            'expectedResult': [1]
        })

        start = None
        self._arguments.append({
            'root': start,
            'expectedResult': []
        })

        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertEqual(argument['expectedResult'], actual_result)
