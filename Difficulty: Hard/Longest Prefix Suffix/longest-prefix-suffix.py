#User function Template for python3

class Solution:
	def lps(self, str):
	    i = 0
	    count = 0
	    k , j = 1,1
	    while i < len(str) and j < len(str):
	        if str[i] == str[j]:
	            i += 1
	            j += 1
	            count += 1
	        else:
	            i = 0
	            j = k
	            k += 1
	            count = 0
	    return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends