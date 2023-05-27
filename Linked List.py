# Loc Lien Algorithms and Data Structures Refresher Course
# https://www.youtube.com/watch?v=WwfhLC16bis&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=5 
# ===================
# Linked List
# ===================

class LinkedListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.end = None
    def insert(self,val) -> None:
        # Checking to see if our linked list already has values within the reference list
        if self.head and self.end:
            #print("Inserted value {} into the linked list".format(val))
            self.end.next = LinkedListNode(val)
            self.end = self.end.next
        # If the list is empty
        else:
            #print("Inserted value {} into the linked list".format(val))
            self.head = LinkedListNode(val)
            self.end = self.head

    def delete(self,val) -> None:
        currNode = self.head
        delFlag = False
        # If the head node's value is the same as the value to be deleted
        # Removes the reference to current matched head by setting the class head
        # to currNode.next, effectively removing the value from the linked list. 
        if currNode.val == val:
            self.head = currNode.next
            delFlag = True
        while currNode.next and not delFlag:
            if currNode.next.val == val:
                currNode.next = currNode.next.next 
                delFlag = True
            else:
                currNode = currNode.next
        if delFlag:
            print("Successfully removed {} from the linked list".format(val))
        else:
            print("Could not find {} in the linked list".format(val))
        
    def reverse(self):
        if not self.head:
            print("Please insert a node before reversing the linked list")
        else:

            prevNode = None
            while self.head:
                temp = self.head.next
                self.head.next = prevNode
                prevNode = self.head
                self.head = temp
                #print(self.printLinkedList())
            self.head = prevNode
                
    def printLinkedList(self):
        #print("DEBUG ENTERED PRINTLINKEDLIST")
        currNode = self.head
        retArr = []
        while currNode:
            #print("Current Node's Value: {}".format(currNode.val))
            retArr.append(currNode.val)
            currNode = currNode.next
        return retArr
    
    def findValue(self,target):
        currNode = self.head
        while currNode:
            if currNode.val == target:
                return True
            else:
                currNode = currNode.next
        return False
               
# Function to count the number of nodes in the linked list's reference head
def countNodes(head):
    currNode = head
    counter = 0
    while currNode:
        counter += 1
        currNode = currNode.next   
    return counter

def main():
    linkedListOne = LinkedList()
    linkedListVals = [1,2,3,4,5,6]
    for i in linkedListVals:
        linkedListOne.insert(i)
    print(countNodes(linkedListOne.head))
    print(linkedListOne.printLinkedList())
    linkedListOne.delete(6)
    print("Removed Test {}".format(linkedListOne.printLinkedList()))
    linkedListOne.reverse()
    print("Reverse Test {}".format(linkedListOne.printLinkedList()))
    print(linkedListOne.findValue(1))
    print(linkedListOne.findValue(10))


main()

