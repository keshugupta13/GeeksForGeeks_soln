#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        if head is None:
            return [None,None]
        if head and head.next is None:
            return [head,None]
        h1=head
        h2=head.next
        temp1=h1
        temp2=h2
        
        while temp1 and temp2:
            temp1.next=temp2.next
            temp1=temp1.next
            
            if temp1:
                temp2.next = temp1.next
                temp2 = temp2.next
            
                
        return [h1,h2]
        
        #Your code here
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends