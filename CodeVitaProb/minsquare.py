for t in range(int(input())):
    
    n= int(input())
    x,y=[],[]
    
    for i in range(n):    
        cord=list(map(int,input().split()))
        x.append(cord[0])
        y.append(cord[1])
        
    x1,x2=max(x),min(x)
    y1,y2=max(y),min(y)
    l1=x1-x2
    l2=y1-y2
    
    print(max(l1,l2)**2)
