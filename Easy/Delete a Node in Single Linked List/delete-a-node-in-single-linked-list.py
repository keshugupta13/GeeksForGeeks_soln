# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    if head is None:
        return head

    if k == 1:
        return head.next

    prev = None
    current = head
    count = 1

    while current is not None and count != k:
        prev = current
        current = current.next
        count += 1

    if current is None:
        return head

    prev.next = current.next

    return head
#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
            self.last = self.head
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.last.next = new_node
            self.last = new_node
            # self.
            # temp = self.head
            # while(temp.next):
            #     temp=temp.next
            # temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends