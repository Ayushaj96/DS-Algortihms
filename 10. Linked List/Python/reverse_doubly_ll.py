import gc
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # function to find length
    def length(self):
        temp = self.head
        count = 0
        while(temp != None):
            temp = temp.next
            count += 1
        return count

    # function to insert in doubly linked list
    def insert(self, data, pos):
        if pos < 0 or pos > self.length():
            return
        
        # insert at beginning
        if pos == 0:
            # if list is empty
            if self.head == None:
                self.head = Node(data)
            # if list is not empty
            else:
                n = Node(data)
                n.next = self.head
                n.prev = None
                self.head.prev = n 
                self.head = n 
        # insert in middle or end
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            if temp.next:
                temp.next.prev = n 
            temp.next = n

    # function to reverse doubly linked list
    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        
        temp = self.head
        while temp:
            p = temp.next
            temp.next = temp.prev 
            temp.prev = p 
            if temp:
                self.head = temp
            temp = temp.prev

    # function to print doubly linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

# main driver function
if __name__ == '__main__':
    ll = DoublyLinkedList()
    arr = list(map(int, input().split()))
    for i, num in enumerate(arr):
        ll.insert(num, i)
    
    ll.printList()
    ll.reverse()
    ll.printList()