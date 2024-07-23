#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        f0 = 0
        f1 = 0
        f2 = 0
        
       
        for i in arr:
            if i == 0:
                f0 += 1
            elif i == 1:
                f1 += 1
            else:
                f2 += 1

     
        i = 0
        for j in range(1, f0 + 1):
            arr[i] = 0
            i += 1
        for j in range(1, f1 + 1):
            arr[i] = 1
            i += 1
        for j in range(1, f2 + 1):
            arr[i] = 2
            i += 1
      
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends