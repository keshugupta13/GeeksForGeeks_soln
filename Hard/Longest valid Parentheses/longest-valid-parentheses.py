# User function Template for Python3

class Solution:
    def maxLength(self, S):
        stack=[]
        length=0
        stack.append(-1)
        n=len(S)
        for i in range(n):
            if S[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = max(length,i-stack[-1])
        return length
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends