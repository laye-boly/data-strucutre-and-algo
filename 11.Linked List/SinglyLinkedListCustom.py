class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def addNode(self, value, position):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            if position == 0:
                new_node.next = self.head
                self.head = new_node
            elif position == 1:
                self.tail.next = new_node
                self.tail = new_node
            
            else:
                current_node = self.head
                index = 0
                previous_node = None
                while index < position - 1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node

        self.length += 1
    
    def traverseSLL(self):
        if self.head is None:
            print('List is empty : cant traversal it')
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next

    def searchValue(self, value):
        if self.head is None:
            print('List is empty')
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.value == value:
                    return 'your value is inside the Single Simple List'
                else:
                    current_node = current_node.next
            return 'your value is not inside the Single Simple List'
    
    def deleteValue(self, position):
        if self.length < position:
            print("Aucun élément n'est à cette postion")
        elif self.head is None:
            print('List is empty')
           
        else:
            if position == 0:
                
                self.head = self.head.next
            elif position == 1:
                current_node = self.head
                while current_node.next.next is not None:
                    current_node = current_node.next
                self.tail = current_node
                self.tail.next = None
            else:
                index = 0
                current_node = self.head
                while index < position - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
        self.length -= 1

    def deleteEntireSLL(self):
        if self.head is None:
            print('List is empty')
        else:
            self.head = None
            self.tail = None
            

                
                
    


single_node = SimpleLinkedList()
single_node.addNode(1, 1)
single_node.addNode(3, 1)
single_node.addNode(3, 1)
single_node.addNode(2, 1)
#single_node.addNode(0, 0)
#single_node.addNode(0, 4)
#print([node.value for node in single_node])
single_node.traverseSLL()
#print(single_node.searchValue(1))
#rint('start delete')
#single_node.deleteValue(0)
#ingle_node.traverseSLL()
#print('---------------------')
#single_node.deleteValue(1)
#ingle_node.traverseSLL()
#print('---------------------')
#single_node.deleteValue(2)
#single_node.traverseSLL()
#print('---------------------')
#single_node.deleteValue(5)
single_node.deleteEntireSLL()
single_node.traverseSLL()
           
            




