#User function Template for python3

class Solution:
    def fibSum (self,N):
        if N < 2:
            return N
            
        f1 = 0
        f2 = 1
        res = 1
        for _ in range(2, N+1):
            f1, f2 = f2, (f1+f2) % 1000000007
            res += f2 
        return res % 1000000007

        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))
# } Driver Code Ends