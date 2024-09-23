#User function Template for python3

class Solution:
    def findTwoElement( self,arr):
        n = len(arr)
        mp = {}
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            if arr[i] not in mp:
                mp[arr[i]] = 1
            else:
                mp[arr[i]] += 1
            
        repeat = 0
        for key,value in mp.items():
            if value > 1:
                repeat = key
                break
        
        actual_sum = n * (n + 1) // 2
        missing = actual_sum - (curr_sum - repeat)
        
        return repeat, missing


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends