#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        i,j = 0 ,0
        arr=[]
        while i<n and j<m:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
                
        while i <n:
            arr.append(arr1[i])
            i+=1
        
        while j <m:
            arr.append(arr2[j])
            j += 1
            
        return arr[k-1]
                
            
                
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends