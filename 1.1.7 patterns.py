# pattern 1
"""

*****
*****
*****
*****
*****

""" 
class Solution:
    def printSquare(self, N):
        [print("* "*(N)) for i in range(N)]

# pattern 2
"""

*
**
***
****
*****

"""

class Solution:
    def printTriangle(self, N):
        [print("* "*(i)) for i in range(1,N+1)]

# pattern 3
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            [print("{}".format(j),end=" ") for j in range(1,i+1)]
            print()

# pattern 4
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print("{}".format(i),end=" ")
            print()

#pattern 5
"""
*****
****
***
**
*
"""
class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            print("* "*i)

#pattern 6
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()