
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
         curr, ans = 0, 0
         for item in arr:
             if item <= k:
                 curr += item
             else:
                 ans = max(ans, curr)
                 curr = 0
         ans = max(ans, curr)  # To handle the case where the largest sum is at the end of the array
         return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends