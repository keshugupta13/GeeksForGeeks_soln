#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    right = len(S)-1
        left = 0
        
        while left < right:
            if S[left] == S[right]:
                left += 1
                right -= 1
            else:
                return 0
                
        return 1
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends