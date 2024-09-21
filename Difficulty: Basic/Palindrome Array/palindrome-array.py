
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        left = 0
        right = len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True
                
        # code here
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.isPerfect(arr)

        if res:
            print("true")
        else:
            print('false')

# } Driver Code Ends