#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        ans=n-1
        c=m
        for i in range(0,n):
            count=0
            for j in range(0,m):
                if(a[i][j]==1):
                    count+=1
                    
            if(count<c):
                ans=i
                c=count
            elif(count==c):
                ans=min(ans,i)
        return ans+1
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends