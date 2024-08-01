class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        top,bottom,left,right = 0,n-1,0,m-1
        while(top<=bottom and left<=right):
            ##traverse right
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top += 1
            
            #traverse down
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right -= 1
            
            
            ## traverse left
            if top<= bottom:
                
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
                
            ## traverse up
            if left <= right:
                for j in range(bottom,top-1,-1):
                    ans.append(matrix[j][left])
                left += 1
            
        return ans
                
                
        
        
        
            
                
        
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends