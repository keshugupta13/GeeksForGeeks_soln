class Solution:
    
    # Function to find a solved Sudoku. 
    def SolveSudoku(self, grid):
        
        def solve():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    # Check if the cell is empty
                    if grid[i][j] == 0:
                        for c in range(1, 10):  # Try numbers from 1 to 9
                            if is_valid(i, j, c):
                                grid[i][j] = c
                                
                                if solve():
                                    return True
                                else:
                                    # Backtracking
                                    grid[i][j] = 0
                        return False
            return True
            
        def is_valid(row, col, c):
            for i in range(9):
                if grid[i][col] == c:
                    return False
                if grid[row][i] == c:
                    return False
                if grid[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            return True
        
        return solve()
    
    # Function to print grids of the Sudoku.    
    def printGrid(self, arr):
        for row in range(9):
            for col in range(9):
                print(arr[row][col], end=" ")
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends