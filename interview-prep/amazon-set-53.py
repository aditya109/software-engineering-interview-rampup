"""
Given a String s and int r , first fill each character row wise and print column wise.
for e.g. String s = “abcdefgh” and r = 3
so filling column wise would give :
a d g
b e h
c f

a b c
d e f
g h
"""


def build_custom_string(s, r):
    custom_string = []
    row = ["" for _ in range(r)]
    row_index = 0
    for index in range(len(s)):
        row[row_index] = s[index]
        row_index += 1
        if (index + 1)%r == 0:
            custom_string.append(row)
            row = ["" for _ in range(r)]
            row_index = 0
    custom_string.append(row)

    for i in range(len(custom_string[0])):
        for j in range(len(custom_string)):
            print("{0} ".format(custom_string[j][i]), end="")
        print()
        
    
# build_custom_string("abcdefgh", 3)
"""
given a string or say number .. for e.g. 134 now with each number ,
as per mobile’s keypad , some letters would be associated.
here 1 – > abc , 3->ghi, 4 ->jkl .
So we should print all the permutation such that
we take 1 character from each of the number.
input number can be of any arbitrary length.
lets say each digit has m numbers associated ,
then for the input of length n , we need to generate n^m possible strings.
"""
