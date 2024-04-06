#User function template for Python 3

#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
            candidate = 0
            count = 0
    
   
            for num in A:
                if count == 0:
                    candidate = num
                    count = 1
                elif num == candidate:
                    count += 1
                else:
                    count -= 1
   
            count = 0
            for num in A:
                if num == candidate:
                    count += 1
    
            if count > N // 2:
                return candidate
            else:
                return -1  
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends