#User function Template for python3

def largest( arr, n):
    max_element = arr[0]
    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends