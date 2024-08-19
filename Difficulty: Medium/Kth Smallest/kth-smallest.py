#User function Template for python3


class Solution:
    def partition(self,arr,p,q):
            i = p
            pivot = arr[p]
            for j in range(p + 1, q + 1):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[p] = arr[p], arr[i]
            return i

    def kthSmallest(self, arr, k):
        p = 0
        q = len(arr) - 1
        k -= 1  
        
        while p <= q:
            m = self.partition(arr, p, q)
            if m == k:
                return arr[m]
            elif m < k:
                p = m + 1  
            else:
                q = m - 1  
                
        return -1   

         
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends