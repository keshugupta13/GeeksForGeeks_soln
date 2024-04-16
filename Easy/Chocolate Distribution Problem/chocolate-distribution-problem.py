#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i, j = 0, M-1
        min_diff = float("inf")
        
        while j < N:
            curr_diff = A[j] - A[i]
            min_diff = min(min_diff, curr_diff)
            i += 1
            j += 1
        
        return min_diff



        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends