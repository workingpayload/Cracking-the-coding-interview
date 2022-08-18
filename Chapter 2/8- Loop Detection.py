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

    def loopdetection(self):
        slow = fast = self.head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    ll1 = ll()
    ll1.insert_values([1,2,3])
    ll1.loopdetection()


