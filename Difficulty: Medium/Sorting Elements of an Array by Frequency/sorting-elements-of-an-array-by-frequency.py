#User function Template for python3
from collections import Counter
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        freq = Counter(arr)
        
        def custom_sort(n):
            return (-freq[n], n)
            
        arr.sort(key=custom_sort)
        return arr
        
        
        
        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends