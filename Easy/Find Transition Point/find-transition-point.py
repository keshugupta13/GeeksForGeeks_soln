class Solution:
    def transitionPoint(self, arr, n):
         if n == 1 and arr[0] == 0:
            return -1
         elif n == 1:
            return 0
            
        
         right = n - 1
         left = 0
        
         while left < right:
             search_at_index = (left + right) // 2
             if arr[search_at_index] == 1:
                 right = search_at_index
             else:
                 left = search_at_index + 1
                
        
         if right == 0:
             return 0
         elif right == n - 1:
             return -1
         else:
             return right
        # Code here


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends