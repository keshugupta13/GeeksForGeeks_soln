#User function Template for python3
class Solution:
    def isValid(self, str):
        s = str.split(".")
        if len(s) != 4:
            return 0
        
        for i in s:
            if (len(i) > 3 or len(i)) == 0:
                return 0
            
            if (i[0] == "0" and len(i) > 1):
                return 0
                
            
            k = int(i)
            if(k > 255 or k < 0):
                return 0
        return 1
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends