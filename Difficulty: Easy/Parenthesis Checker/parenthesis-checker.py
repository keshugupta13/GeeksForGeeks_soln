#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        if len(x)%2!=0:
            return  False
            
        if x[0]=="}" or x[0]== ")" or x[0]=="]":
            return False
            
        if x[len(x)-1] == "{" or x[len(x)-1] == "[" or x[len(x)-1] == "(":
            return False
        # code here
        stack=[]
        for i in x:
            if i=="{" or i=="(" or i=="[":
                stack.append(i)
            
            else:
                if len(stack) == 0:
                    return False
                if i=="]":
                    if stack[len(stack)-1]=="[":
                        stack.pop()
                    else:
                        return False
                        
                elif i=="}":
                    if stack[len(stack)-1]=="{":
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[len(stack)-1]=="(":
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")

# } Driver Code Ends