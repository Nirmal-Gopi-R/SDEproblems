def LRS( str):  
  
    n = len(str)   
    dp=[[0]*(n+1)]*(n+1)   
    for i in range(1,n+1): 
        for j in range(1,n+1): 
            # check whether the characters are same 
            if (str[i-1] == str[j-1] and i != j):  
                dp[i][j] = 1 + dp[i-1][j-1]          
                          
            #if the characters are not same  
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])  
          
      
    return dp[n][n]  
  
  

str = "aabb"
print(LRS(str)) 
