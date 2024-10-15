#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        sum1 = 0
        count = 0
        mp = {}
        for i in range(len(arr)):
            sum1 += arr[i]
            if sum1 == tar:
                count += 1
                
            if (sum1-tar) in mp:
                count += mp[sum1-tar]
                
            if sum1 in mp:
                mp[sum1] += 1
            else:
                mp[sum1] = 1
                
        return count
        
            
            
        #Your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends