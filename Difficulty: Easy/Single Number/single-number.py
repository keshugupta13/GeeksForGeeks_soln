#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        n = len(arr)
        mp={}
        for i in range(n):
            if arr[i] not in  mp:
                mp[arr[i]] = 1
            else:
                mp[arr[i]] += 1
                
        for i in range(n):
            if mp[arr[i]] % 2 != 0:
                return arr[i]
        
        # code here


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends