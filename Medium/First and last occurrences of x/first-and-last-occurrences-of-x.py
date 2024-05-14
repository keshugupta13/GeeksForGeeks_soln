#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        a=[]
        if x not in arr:
                return -1,-1
        for i in range(n):
            if arr[i]==x:
                a.append(i)
        return a[0],a[len(a)-1]
        
        # code here


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends