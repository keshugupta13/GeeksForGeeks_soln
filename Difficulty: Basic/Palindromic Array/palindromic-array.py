# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        palindrome = 0
        original = temp
        while temp != 0:
            rem = temp % 10
            palindrome = palindrome * 10 + rem
            temp //= 10 
        
        if original != palindrome:
            return False  
    return True
        
    # Code here



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends