class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        left_small = [0] * n
        right_small = [0] * n
        stack=[]
        stack.append(0)
        for i in range(n):
            while stack and arr[i] <= stack[-1]:
                stack.pop()
            left_small[i] = stack[-1]
            stack.append(arr[i])
        stack.clear()
        
        stack.append(0)
        for i in range(n-1,-1,-1):
            while stack and arr[i] <= stack[-1]:
                stack.pop()
            right_small[i] = stack[-1]
            stack.append(arr[i])
            
        ans = 0
        for i in range(n):
            ans = max(ans,abs(left_small[i] - right_small[i]))
        return ans
                
        
        
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends