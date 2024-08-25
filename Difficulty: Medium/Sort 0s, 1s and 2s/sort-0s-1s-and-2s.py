#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        count_0 = 0
        count_1 = 0
        count_2 =0 
        for i in range(n):
            if arr[i] == 0:
                count_0  += 1
            
            elif arr[i] == 1:
                count_1 += 1
                
            else:
                count_2 +=1
                
        i = 0
        for j in range(count_0):
            arr[i] = 0
            i += 1
            
        for j in range(count_1):
            arr[i] = 1
            i += 1
            
        for j in range(count_2):
            arr[i] = 2
            i += 1
            
        
        # code here



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