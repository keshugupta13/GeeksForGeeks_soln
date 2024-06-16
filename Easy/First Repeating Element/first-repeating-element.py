#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        dict={}
        
        for x in arr:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        
        count = 1
        for i in arr:
            if (dict[i]>1):
                return count
            count+=1
                
        return -1
        
        
        #arr : given array
        #n : size of the array


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends