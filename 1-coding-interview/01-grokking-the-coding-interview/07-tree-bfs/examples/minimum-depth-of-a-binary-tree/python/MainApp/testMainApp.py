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
                'expectedResult': 5
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
                'expectedResult': 2
            }
        )
        start = TreeNode(1)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': 1
            }
        )
        start = None
        self._arguments.append(
            {
                'root': start,
                'expectedResult': 0
            }
        )
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertEqual(argument['expectedResult'], actual_result)
