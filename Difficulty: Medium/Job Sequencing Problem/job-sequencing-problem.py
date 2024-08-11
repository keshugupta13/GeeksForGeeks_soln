#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        maxdeadline = -1
        arr=[]
        totalprofit = 0
        counter = 0

        
        for i in range(n):
            maxdeadline = max(maxdeadline, Jobs[i].deadline)
            
        result = [-1] * maxdeadline
        
        for i in range(n):
            arr.append([Jobs[i].profit, Jobs[i].deadline])
            
        arr.sort(reverse=True)
        for i in range(n):
            for j in range(arr[i][1]-1,-1,-1):
                if result[j] == -1:
                    result[j] = i
                    counter += 1
                    totalprofit += arr[i][0]
                    break
        return[counter , totalprofit]
            
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends