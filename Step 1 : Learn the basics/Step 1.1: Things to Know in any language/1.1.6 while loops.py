#https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

n = input()
i=0
odd,even = 0,0
while len(n)!=i:
    if int(n[i])%2!=0:
        odd+=int(n[i])
    else:
        even+=int(n[i])
    i+=1
print(even," ",odd)


