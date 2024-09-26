#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        count = 0
        maxi = 0
        n = len(arr)
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                count += 1
                maxi = max(maxi,count)
            else:
                count = 0
        return maxi
        
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends