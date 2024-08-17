#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        product = 1
        count_0 = 0
        for i in range(n):
            if nums[i] == 0:
                count_0 += 1
            else:
                product *= nums[i]
                
        for i in range(n):
            if count_0 > 1:
                nums[i] = 0
            
            elif count_0 == 0:
                nums[i] = product // nums[i]
                
            elif count_0 == 1 and nums[i] != 0:
                nums[i] = 0
            
            else:
                nums[i] = product
        return nums
        
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends