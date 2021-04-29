"""
Print all possible words from phone digits
Difficulty Level : Hard
Last Updated : 18 Nov, 2020
Before the advent of QWERTY keyboards, 
texts and numbers were placed on the same key. 
For example, 2 has “ABC” if we wanted to write anything starting with ‘A’ 
we need to type key 2 once. 
If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. 


"""


hashTable = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]


def printWordsUtil(number, curr, output, n):
    if(curr == n):
        print(output)
        return

    # Try all 3 possible characters
    # for current digir in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output, n)
        output.pop()
        if(number[curr] == 0 or number[curr] == 1):
            return


n = 234
n = [int(i) for i in str(n)]
print(printWordsUtil(
    number=n,
    curr=0,
    output=[],
    n=len(n)
))
