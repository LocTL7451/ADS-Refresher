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
            print("Inserted value {} into the linked list".format(val))
            self.end.next = LinkedListNode(val)
            self.end = self.end.next
        # If the list is empty
        else:
            print("Inserted value {} into the linked list".format(val))
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
        if delFlag:
            print("Successfully removed {} from the linked list".format(val))
        else:
            print("Could not find {} in the linked list".format(val))
        
    def printLinkedList(self):
        #print("DEBUG ENTERED PRINTLINKEDLIST")
        currNode = self.head
        retArr = []
        while currNode:
            print("Current Node's Value: {}".format(currNode.val))
            retArr.append(currNode.val)
            currNode = currNode.next
        return retArr
               
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
    linkedListVals = [6,3,4,2,1]
    for i in linkedListVals:
        linkedListOne.insert(i)
    print(countNodes(linkedListOne.head))
    print(linkedListOne.printLinkedList())
    linkedListOne.delete(6)
    print("TEST {}".format(linkedListOne.printLinkedList()))
main()

