import unittest

from app.mainApp import MainApp, TreeNode


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._arguments = list()
        r = TreeNode(5)
        r.left = TreeNode(4)
        r.left.left = TreeNode(11)
        r.left.left.left = TreeNode(7)
        r.left.left.right = TreeNode(2)

        r.right = TreeNode(8)
        r.right.left = TreeNode(13)
        r.right.right = TreeNode(4)
        r.right.right.right = TreeNode(1)

        self._arguments.append(
            {
                'root': r,
                'targetSum': 22,
                'expectedResult': True
            }
        )
        self._arguments.append({
            'root': r,
            'targetSum': 18,
            'expectedResult': True
        })
        self._arguments.append({
            'root': r,
            'targetSum': 17,
            'expectedResult': False
        })

        r = TreeNode(5)
        r.left = TreeNode(4)
        r.right = TreeNode(8)
        self._arguments.append({
            'root': r,
            'targetSum': 29,
            'expectedResult': False
        })
        self._arguments.append({
            'root': r,
            'targetSum': 9,
            'expectedResult': True
        })
        r = TreeNode(1)
        r.left = TreeNode(2)
        self._arguments.append({
            'root': r,
            'targetSum': 0,
            'expectedResult': False
        })
        self._mainAppInstance = MainApp()

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['root'], argument['targetSum'])
            self.assertEqual(argument['expectedResult'], actual_result)
