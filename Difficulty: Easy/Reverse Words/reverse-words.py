# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        stack = []
        word = ""
    
    # Traverse the string and split words
        for char in s:
            if char != '.':
                word += char
            elif word:
                stack.append(word)
                word = ""
    
        if word:
            stack.append(word)
    
    # Build the result string by popping from the stack
        result = ""
        while stack:
            result += stack.pop()
            if stack:
                result += "."
    
        return result


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends