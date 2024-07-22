#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        res = []
        
        i = 0
        while i <n:
            arr = []
            j = 0
            while j <= k and i < n:
                arr.append(a[i])
                i += 1
                j += 1
            arr.sort()
            res = res + arr
        return res
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends