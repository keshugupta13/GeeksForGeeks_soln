#User function Template for python3
class Solution:
	def removeDups(self, S):
	    res=""
		for i in S:
		    if i not in res:
		        res+=i
        return res
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends