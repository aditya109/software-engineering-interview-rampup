import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = []
        start = TreeNode(5)
        start.left = TreeNode(2)
        start.left.left = TreeNode(1)
        start.left.right = TreeNode(4)
        start.left.right.left = TreeNode(6)
        start.left.right.right = TreeNode(8)
        start.right = TreeNode(3)
        self._arguments.append(
            {
                'root': start,
                'k': [5, 1, 4, 8],
                'expectedResult': False
            }
        )
        self._arguments.append(
            {
                'root': start,
                'k': [5, 2, 4, 8],
                'expectedResult': True
            }
        )
        self._arguments.append(
            {
                'root': start,
                'k': [5, 3, 4, 9],
                'expectedResult': False
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'], argument['k'])
            self.assertEqual(argument['expectedResult'], actual_result)
