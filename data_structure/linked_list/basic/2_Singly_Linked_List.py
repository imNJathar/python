
# This class is used to create new node for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.NextNode = None

# This class is used to handle all functionalilty of singly linked list
class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    # Function to create new node from class Node
    def _createNode(self, data):
        self.newNode = Node(data)

    # This function insert node at start of list
    def insertAtStart(self, data):
        self._createNode(data)
        temp = self.head
        self.head = self.newNode
        self.newNode.NextNode = temp

    # This function insert node at end of list
    def insertAtEnd(self, data):
        self._createNode(data)
        if self.head != None:
            temp = self.head
            while(temp.NextNode != None):
                temp = temp.NextNode
            temp.NextNode = self.newNode
            return
        self.head = self.newNode

    # This function insert node at given number in list other wise end of list
    def insertAtNumber(self, data, number=0):
        if number < 0:
            print("Number should be always greater than 0")
            return
        cnt = 1
        if number == cnt:
            self.insertAtStart(data)
        elif number == 0:
            self.insertAtEnd(data)
        else:
            temp = self.head
            while cnt != number - 1:
                if temp.NextNode == None:
                    break
                temp = temp.NextNode
                cnt += 1
            self._createNode(data)
            self.newNode.NextNode = temp.NextNode
            temp.NextNode = self.newNode
    
    # This function delete node at start of list
    def deleteAtStart(self):
        temp = self.head
        self.head = self.head.NextNode
        del temp        

    # This function delete node at end of list
    def deleteAtEnd(self):
        temp = self.head
        temp1 = temp
        while(temp.NextNode != None):
            temp1 = temp
            temp = temp.NextNode
        temp1.NextNode = None
        del temp
    
    # This function delete node at given numbe in list otherwise end of the list
    def deleteAtNumber(self, number=0):
        if number < 0:
            print("Number should be always greater than 0")
            return
        cnt = 1
        if number == cnt:
            self.deleteAtStart()
        elif number == 0:
            self.deleteAtEnd()
        else:
            temp = self.head
            while(cnt != number-1):
                if temp.NextNode == None:
                    break
                prevNode = temp
                temp = temp.NextNode
                cnt += 1
            if temp.NextNode == None:
                prevNode.NextNode = None
                del temp
            else:
                temp1 = temp.NextNode
                temp.NextNode = temp1.NextNode
                temp1.NextNode = None
                del temp1

    # This function display's node of list
    def displayList(self):
        temp = self.head
        while(temp.NextNode != None):
            print("| {} | --> ".format(temp.data), end="")
            temp = temp.NextNode
        print("| {} |".format(temp.data))

    def opration(self):
        print("Inserting node at end of the linked list")
        self.insertAtEnd("Monday")
        self.insertAtEnd("Tuesday")
        self.insertAtEnd("Wednesday")
        self.insertAtEnd("Thursday")
        self.insertAtEnd("Friday")

        self.displayList()

        print("\nInserting node at start of the linked list")
        self.insertAtStart("Sunday")
        self.displayList()

        print("\nInserting node at given number in the linked list")
        self.insertAtNumber("Saturday", 7)
        self.displayList()

        print("\nDeleting node from start of the linked list")
        self.deleteAtStart()
        self.displayList()

        print("\nDeleting node from end of the linked list")
        self.deleteAtEnd()
        self.displayList()

        print("\nDeleting node from given number in linked list")
        self.deleteAtNumber(3)
        self.displayList()

def main():
    obj = SinglyLinkedList()
    obj.opration()

if __name__ == "__main__":
    main()