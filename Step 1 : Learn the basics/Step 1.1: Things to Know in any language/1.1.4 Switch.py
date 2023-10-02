#https://www.codingninjas.com/studio/problems/switch-case-statement_8357244?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""In python, there are no switch statement. Hence, the default if-else case applies."""

from typing import *
from math import pi

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch == 1:
        return round(pi*a[0]**2,5)
    else:
        return "{:.5f}".format(a[0]*a[1])