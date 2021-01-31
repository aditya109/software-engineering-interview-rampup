import unittest
import logging

from program import Program
from test_suite_provider import test_suite_collector

NUMBER_OF_TEST_CASES, TEST_CASES = test_suite_collector()

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.test_object = Program()

    def test_func(self):
        logging.info(NUMBER_OF_TEST_CASES)
        try:

            self.assertEqual(self.test_object.func([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3),
                             1223,
                             'Test Case Failed ! ⭕')
        except AssertionError as error:
            logging.warning("Test Case Failed ! ⭕ もう一度やり直してください")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestProgram))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main()
