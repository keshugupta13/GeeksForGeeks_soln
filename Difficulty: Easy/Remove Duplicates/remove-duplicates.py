#User function Template for python3
class Solution:
	def removeDups(self, str):
	    res = []
	    for i in str:
	        if i not in res:
	            res += i
	    return "".join(res)
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends