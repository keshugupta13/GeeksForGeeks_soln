#User function Template for python3

class Solution:
    
    def knapSack(self,W, wt, val):
        n = len(wt)
        dp=[]
        for i in range(n+1):
            dp.append([0]*(W+1))
        for i in range(1,n+1):
            for j in range(1,W+1):
                if(wt[i-1]<=j):
                    dp[i][j]=max(val[i-1]+ dp[i-1][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][W]
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends