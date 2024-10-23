#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
        
        
        
    def sumOfLastN_Nodes(self, head, n):
        sum1 = 0
        head = self.reverse(head)
        
        while n > 0 and head:
            sum1 += head.data
            head = head.next
            n -= 1
            
        return sum1
        
        
            
            
        
        
        #function should return sum of last n nodes


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

# } Driver Code Ends