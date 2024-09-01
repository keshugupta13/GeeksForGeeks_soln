#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        i, j = 0, 0
        sum1, sum2 = 0, 0
        ans = 0

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                ans += max(sum1, sum2) + arr1[i]
                i += 1
                j += 1
                sum1, sum2 = 0, 0

        while i < n:
            sum1 += arr1[i]
            i += 1

        while j < m:
            sum2 += arr2[j]
            j += 1

        ans += max(sum1, sum2)
        return ans
        # Code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends