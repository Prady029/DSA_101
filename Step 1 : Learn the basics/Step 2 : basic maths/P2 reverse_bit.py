#https://www.codingninjas.com/studio/problems/reverse-bits_2181102?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def reverseBits(n):
    # Write your code here.
    return int(str(format(n, 'b').zfill(32)[::-1]),2)