# https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Read input as specified in the question.
# Print output as specified in the question.

def inp_type(inp):
    if not inp.isalpha():
        print(-1)
    elif inp.islower():
        print(0)
    else:
        print(1)


inp = input().split()[-1]
inp_type(inp)