#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        arr =[]
        i,j = 0,0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
            
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
            
        n = len(arr)
        mid1 = arr[(n//2) - 1]
        mid2 = arr[n//2]
        
        return mid1 + mid2
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends