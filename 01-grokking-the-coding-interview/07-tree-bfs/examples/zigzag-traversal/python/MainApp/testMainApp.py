import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()
        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)

        start.left.left = TreeNode(4)
        start.left.right = TreeNode(5)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': [[1], [3, 2], [4, 5]]
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
                'expectedResult': [[3], [20, 9], [15, 7]]
            }
        )
        start = TreeNode(1)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': [[1]]
            }
        )
        start = None
        self._arguments.append(
            {
                'root': start,
                'expectedResult': []
            }
        )

        start = TreeNode(1)
        start.left = TreeNode(2)
        start.right = TreeNode(3)

        start.left.left = TreeNode(4)
        start.right.right = TreeNode(5)
        self._arguments.append(
            {
                'root': start,
                'expectedResult': [[1], [3, 2], [4, 5]]
            }
        )
        self._mainAppInstance = MainApp()

    @staticmethod
    def is_equal(list1, list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'])
            self.assertTrue(self.is_equal(argument['expectedResult'], actual_result))
