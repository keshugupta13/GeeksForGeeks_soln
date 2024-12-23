#User function Template for python3
class Solution:
    def onesComplement(self,num):
        def decimal_to_binary(num):
            if num == 0:
                return "0"
            binary = ""
            while num > 0:
                rem = num % 2
                binary = str(rem) + binary
                num = num // 2 
            return binary
        
        def binary_to_decimal(binary):
            decimal = 0
            binary_str = binary[::-1]
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        binary = decimal_to_binary(num)
        n = len(binary)

        complement = ''
        for i in range(n):
            if binary[i] == '0':
                complement += '1'
            else:
                complement += '0'

        return binary_to_decimal(complement)

        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.onesComplement(N))
# } Driver Code Ends