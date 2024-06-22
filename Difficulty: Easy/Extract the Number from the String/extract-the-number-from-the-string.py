class Solution:
    def ExtractNumber(self,sentence):
        ans = -1
        for word in sentence.split():
            if '9' not in word:
                try:
                    num = int(word)
                    ans = max(ans, num)
                except ValueError:
                    pass
        return ans
        #code here


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends