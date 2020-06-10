import itertools as it
import numpy as nu
#l=list(map(int,input()))
#k=int(input())
l=[1,2,3,4]
k=10
c=0
f=0
for i in range(1,4):
    print(i)
    for j in it.combinations(l,i):
        p=nu.prod(j)
        if p<k:
            print(j)
            c+=1
        else:
            print(j)
            f=1
    if f==1:
        break
print(c)
        
