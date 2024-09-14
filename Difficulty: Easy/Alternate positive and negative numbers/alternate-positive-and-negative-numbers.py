#User function Template for python3

class Solution:
    def rearrange(self,arr):
        positive = []
        negative = []
    
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
    
        i, j, k = 0, 0, 0
        while i < len(arr):
            if j < len(positive):
                arr[i] = positive[j]
                i += 1
                j += 1
            if k < len(negative):
                arr[i] = negative[k]
                i += 1
                k += 1  
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends