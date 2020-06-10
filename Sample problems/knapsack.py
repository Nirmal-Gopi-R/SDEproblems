#we get size of the bag and number of items in the bag
size=int(input())
n=int(input())
#profit and size of each item
pro=list(map(int,input().split()))
weight=list(map(int,input().split()))
# to find the correct profit according to weight we find Pro[i]/weight[i]
res=[]
for i in range(len(pro)):
    res.append(pro[i]/weight[i])
hash=[0 for i in range(n)]
while(1):
    m=max(res)
    s=weight[res.index(m)]
    if s<size:
        size-=s
        hash[res.index(m)]=1
        res[res.index(m)]=0
    else:
        hash[res.index(m)]=size/weight[res.index(m)]
        size=0
        res[res.index(m)]=0
    if size==0:
        break
print('the items and quantity of items included in the bag are represented in a value between 0-1',hash)
