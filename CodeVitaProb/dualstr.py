t=int(input())
for x in range(t):
    s=input()
    s1=""
    k=1
    f=0
    while(len(s)>0):
        if s1+s[0] in s[k:]:
            s1+=s[0]
            s=s[k:]
        else:
            if s1 in s[k:]:
                s=s[k:]
            else:
                f=1
                break
        print(s1)
    if f==0:
        print("No")
    else:
        print("Yes")  
            
            
        
