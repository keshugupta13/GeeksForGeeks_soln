#User function Template for python3

class Solution:

    def convert(self, s, n):
        if n ==1 or n >= len(s):
            return s
        
        l = [""]*n
        index = 0
        step = 1
        for i in s:
            l[index] += i
            
            if index == 0:
                step = 1
            elif index == n-1:
                step = -1
            
            index += step
            
        return "".join(l)
             
            
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        n = int(input())

        solObj = Solution()

        print(solObj.convert(Str,n))
# } Driver Code Ends