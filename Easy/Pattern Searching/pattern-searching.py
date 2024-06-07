#User function Template for python3
class Solution:
	def search(self, text, pat):
	    if pat in text:
            return 1
        else:
            return 0
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		text,pat = input().split()
		ob = Solution()
		answer = ob.search(text,pat)
		print(answer)


# } Driver Code Ends