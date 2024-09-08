#User function Template for python3
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n==1:
            return 0
        if arr[0]==0:
            return -1
        step = arr[0]
        jump = 1
        Range = arr[0]
        for i in range(1,n):
            if i==n-1:
                return jump
            Range = max(Range, i+arr[i])
            step-=1
            if step==0:
                jump+=1
                if Range <= i:
                    return -1
                step  = Range - i
        return -1
        #code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends