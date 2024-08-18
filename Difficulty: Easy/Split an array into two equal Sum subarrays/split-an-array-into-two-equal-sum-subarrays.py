class Solution:
    def canSplit(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        
        res = 0
        total_sum = 0
        curr_sum = 0
        for i in arr:
            total_sum += i
            
        for i in range(n):
            curr_sum = curr_sum + arr[i]
            total_sum = total_sum - arr[i]
            if curr_sum == total_sum:
                return 1
            
        return 0
            
        #code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends