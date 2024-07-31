#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        arr.sort()
        first = arr[0]
        last = arr[len(arr)-1]
        n = len(last)
        ans=""
        
        i = 0
        for i in range(n):
            if first[i] != last[i]:
                break
            
            ans += first[i]
        
        if ans:
            return ans
        else:
            return "-1"
                
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends