class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        hmap = dict()
        ans = 0
        for i in range(len(arr)):
            if(arr[i] not in hmap):
                hmap[arr[i]] = i
            else:
                ans = max(ans, i-hmap[arr[i]])
        return ans
        # Code here



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends