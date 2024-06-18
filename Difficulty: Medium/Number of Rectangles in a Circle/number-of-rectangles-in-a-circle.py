#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        ans=0
        for i in range(1,2*r):
            j=(((2*r)**2)-((i)**2))**(1/2)
            ans+=int(j)
        return ans


        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends