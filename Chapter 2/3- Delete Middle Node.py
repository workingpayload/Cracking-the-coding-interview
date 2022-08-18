class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class ll:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_values):
        self.head = None
        for data in data_values:
            self.insert_at_end(data)

    def removeduplicates(self):
        temp = self.head

        while(self.head and self.head.next):
            if self.head.val == self.head.next.val:
                self.head.next = self.head.next.next
            else:
                self.head = self.head.next

        return temp

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr.next:
            llstr += str(itr.val) + '--->'
            itr = itr.next
        llstr += str(itr.val)
        print(llstr)

    def deletenode(self):
        cur = self.head
        
        if not cur or not cur.next:
            return "Failure"
        
        cur.val = cur.next.val
        cur.next = cur.next.next




if __name__ == '__main__':
    ll1 = ll()
    ll1.insert_values([1,2,3])
    ll1.deletenode()
    ll1.print()

