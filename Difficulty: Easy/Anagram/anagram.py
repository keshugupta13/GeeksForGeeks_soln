#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        if len(a) != len(b):
            return False
    
        dict_a = {}
        dict_b = {}

        for char in a:
            if char in dict_a:
                dict_a[char] += 1
            else:
                dict_a[char] = 1
    
        for char in b:
            if char in dict_b:
                dict_b[char] += 1
            else:
                dict_b[char] = 1
    

        return dict_a == dict_b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends