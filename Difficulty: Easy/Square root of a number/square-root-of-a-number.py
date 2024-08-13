#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n):
        left = 0
        right = n
        ans = 0
        while left <= right:
            mid = left + (right-left)//2
            if (mid*mid) == n:
                return mid
            
            elif mid * mid <= n:
                ans = mid
                left = mid+1
            else:
                right = mid - 1
        return ans
        
    #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends