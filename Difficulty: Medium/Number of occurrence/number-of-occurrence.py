#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    count = 0
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                i, j = mid, mid
                while i >= 0 and arr[i] == x:
                    count += 1
                    i -= 1
                while j < len(arr) and arr[j] == x:
                    if j != mid:
                        count += 1
                    j += 1
                break
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return count
	           
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends