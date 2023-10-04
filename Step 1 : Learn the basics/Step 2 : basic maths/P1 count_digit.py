#https://www.codingninjas.com/studio/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countDigits(n: int) -> int:
    return len([i for i in [int(j) for j in str(n) if j!='0'] if n%i == 0])