class Solution:
    def rotateMatrix(self, k, mat):
        mat1 = []
        for i in mat:
            if k%len(i)==k:
                rotate=k
            else:
                rotate = k%len(i)
            mat1.append(i[rotate:]+i[:rotate])
        return mat1
        
        # code here



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends