#https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

n = int(input())
## approch-1
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
## approach - 2
from functools import lru_cache
@lru_cache(maxsize=None) #can control the limit, none == no limit
def fibonacci(n):
    if n==1 or n==2: return 1
    return fibonacci(n-1)+fibonacci(n-2)

## approach - 3 - Binet’s formula
import math
def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    return round(phi**n / sqrt_5)

print(fibonacci(n))

"""In future, if we are to use Dynamic programming or recursion, remember to use LRU_Cache"""