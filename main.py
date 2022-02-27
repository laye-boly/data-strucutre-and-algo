class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        

class CDoubleSimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        if self.length == 1:
            yield node
        else:
            while node:
                yield node
                node = node.next
                if node == self.tail.next:
                    break
            
            

    def createCDSLL(self, value):
        node = Node(value)
        self.head = node
        self.head.next = self.tail
        self.length += 1
    
    def insertCDSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                if self.length == 1:
                    self.tail = self.head
                    newNode.next = self.tail
                    self.tail.previous = newNode
                    self.tail.next = newNode
                    self.head = newNode
                else:
                    newNode.next = self.head
                    self.head.previous = newNode 
                    self.head = newNode 
                    self.tail.next = newNode 
                         
    
            elif location == 1:
                if self.length == 1:
                    newNode.next = self.head
                    newNode.previous = self.head
                    self.tail = newNode
                    self.head.next =  self.tail
                else:
                    newNode.previous = self.tail
                    newNode.next = self.head
                    self.tail.next = newNode
                    self.tail = newNode
                
            else:
                tempNode = self.head
                index = 0
                while index < location - 2:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.previous = tempNode
                newNode.next = nextNode
                nextNode.previous = newNode
                tempNode.next = newNode
                
            self.length += 1

    
    
    def traverseCDSLL(self):
        if self.head is None:
            print('List is empty : cant traversal it')
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value)
                if current_node.next == self.tail.next:
                    break
                current_node = current_node.next
                
    
    def traverseReverseCDSLL(self):
        if self.head is None:
            print('List is empty : cant traversal it')
        
        else:
            current_node = self.tail
            while current_node is not None:
                print(current_node.value)
                if current_node == self.head:
                    break
                current_node = current_node.previous
    
                

    def searchValue(self, value):
        if self.head is None:
            print('List is empty')
        else:
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    return 'your value is inside the Crcular Single Simple List'
                if current_node == self.tail:
                    break

                current_node = current_node.next
                    
            return 'your value is not inside the Circulair Single Simple List'
    
    def deleteValue(self, position):
        if self.length < position:
            print("Aucun élément n'est à cette postion")
        elif self.head is None:
            print('List is empty')
        elif self.length == 1:
            self.tail = None
            self.head = None
           
        else:
            if position == 0:
                self.head = self.head.next
                self.head.previous = None
                self.tail.next = self.head
            elif position == 1:
                current_node = self.head
                while current_node is not None:
                    if current_node == self.tail:
                        current_node.previous.next = self.head
                        self.tail = current_node.previous
                        break
                    current_node = current_node.next
                            
            else:
                index = 0
                current_node = self.head
                while index < position - 2:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.previous = current_node
        self.length -= 1

    

    def deleteEntireCDSLL(self):
        if self.head is None:
            print('List is empty')
        else:
            current_node = self.head
            while current_node is not None:
                current_node.previous = None
                if current_node == self.tail:
                    break
                current_node = current_node.next
            self.head = None
            self.tail = None
            

                
                
    


circularCSLL = CDoubleSimpleLinkedList()
circularCSLL.createCDSLL(1)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(10, 1)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(1, 1)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(5, 2)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(0, 2)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(0, 4)
print([node.value for node in circularCSLL])
circularCSLL.insertCDSLL(20, 0)
print([node.value for node in circularCSLL])
circularCSLL.traverseCDSLL()
circularCSLL.insertCDSLL(40, 4)
print([node.value for node in circularCSLL])
circularCSLL.traverseCDSLL()
print('---------------')
# circularCSLL.traverseReverseCDSLL()
# print(circularCSLL.searchValue(100))
print('start delete')
circularCSLL.deleteValue(0)
circularCSLL.traverseCDSLL()
print('---------------')
circularCSLL.deleteValue(1)
circularCSLL.traverseCDSLL()
print('---------------')
circularCSLL.deleteValue(2)
circularCSLL.traverseCDSLL()

circularCSLL.deleteEntireCDSLL()
circularCSLL.traverseCDSLL()
# circularCSLL.traverseCSLL()

           
            




