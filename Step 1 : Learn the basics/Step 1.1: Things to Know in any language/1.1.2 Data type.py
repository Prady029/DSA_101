# https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

"""In python there is no long, double types, hence, using this dicttionary mapping as the input is a string."""

from typing import *

def dataTypes(type: str):
    t = {'Integer': 4, 'Long': 8, 'Float': 4, 'Double': 8, 'Character': 1}
    return (t[type])
