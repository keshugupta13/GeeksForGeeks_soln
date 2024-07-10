#User function Template for python3

class Solution:
    def findPairs(self, arr, n):
        res = []
        for i in range(n-1):
            for j in range(i+1,n):
                sum1 = arr[i] + arr [j]
                if sum1 in res:
                    return 1
                else:
                    res.append(sum1)
        return 0
        #code here.  



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findPairs(a,n))

# } Driver Code Ends