__author__ = 'rakesh'


#reverse of the linked list

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def traverse(self):

        first = self.head

        while first != None:

            print first.getData()
            first = first.getNext()

    def reverse(self):

        current = self.head

        results = None

        while current != None:

            nextCurrent = current.next
            current.next = results
            results = current
            current = nextCurrent

        self.head = results

        self.traverse()



mylist = UnorderedList()


mylist.add(10)
mylist.add(12)
mylist.add(13)
mylist.add(14)

mylist.reverse()



