# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,s1, s2):
        p_len, s_len = len(pattern), len(string)
        p_ptr, s_ptr = 0, 0  
        star_idx = -1  
        match = 0 
        
        while s_ptr < s_len:
            if p_ptr < p_len and (pattern[p_ptr] == '?' or pattern[p_ptr] == string[s_ptr]):
                p_ptr += 1
                s_ptr += 1
            
            elif p_ptr < p_len and pattern[p_ptr] == '*':
                star_idx = p_ptr
                match = s_ptr
                p_ptr += 1
           
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match += 1
                s_ptr = match
            else:
                return 0
        
        
        while p_ptr < p_len and pattern[p_ptr] == '*':
            p_ptr += 1

        return 1 if p_ptr == p_len else 0

        # Code here



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends