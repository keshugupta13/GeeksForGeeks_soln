#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        low = 0
        high = len(arr) - 1
        n=len(arr)
        if n == 1:
            return arr[0]
        
        if arr[0] != arr[1]:
            return arr[0]
        elif arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
            
        while low <= high:
            mid = (high - low) // 2 + low
            prev = mid - 1
            nxt = mid + 1
                
            if arr[mid] != arr[prev] and arr[mid] != arr[nxt]:
                return arr[mid]
            elif mid % 2 == 0:
                if arr[prev] == arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[prev] == arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return 0

        # Complete this function


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends