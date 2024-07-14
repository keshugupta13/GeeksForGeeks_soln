#User function Template for python3

class Solution:
    def closest3Sum(self, arr, N, target):
        arr.sort()
        closest_sum = float('inf')
        closest_diff = float('inf')
        
        for i in range(0, len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                sum1 = arr[i] + arr[j] + arr[k]
                diff = abs(sum1 - target)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = sum1
                if sum1 == target:
                    return target
                elif sum1 < target:
                    j += 1
                else:
                    k -= 1
        
        return closest_sum
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        X = int(input())
        ob = Solution()
        print(ob.closest3Sum(Arr, N, X))
# } Driver Code Ends