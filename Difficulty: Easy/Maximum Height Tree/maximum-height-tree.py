#User function Template for python3

class Solution:
    def height(self, N):
        i = 1
        res = 1
        while res <= N:
            res += i + 1
            i += 1
        return i - 1
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.height(N))
# } Driver Code Ends