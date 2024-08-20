#User function Template for python3

class Solution:
    def getSpecialNumber(self, n):
        res = 0
        t = n - 1
        w = 1
        while t > 0:
            res += (t % 6) * w
            w *= 10
            t //= 6  
        return res
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.getSpecialNumber(n))
# } Driver Code Ends