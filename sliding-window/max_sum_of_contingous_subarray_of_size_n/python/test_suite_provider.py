import os

NUMBER_OF_ARGS = 3

def test_suite_collector():
        test_cases = []
        dirname = os.path.dirname(__file__)
        f = open(os.path.join(dirname, "test_suite.txt"), "r", encoding='utf-8')
        temp = f.read().split("\n")

        number_of_test_cases  = temp[0]
        temp.pop(0)
        test_case = []
        counter = 0
        for idx, test_line in enumerate(temp):
                counter+=1
                test_case.append(test_line)
                if counter == 3:
                        counter = 0
                        test_cases.append(test_case) 
                        test_case = []
        return number_of_test_cases, test_cases