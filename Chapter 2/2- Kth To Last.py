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

    def print(self,node):
        if node == None:
            print("Linked List is empty")
            return
        itr = node
        llstr = ""
        while itr.next:
            llstr += str(itr.val) + '--->'
            itr = itr.next
        llstr += str(itr.val)
        print(llstr)

    def kth_to_last(self,k):
        p1 = p2 = self.head

        for i in range(k):
            p1 = p1.next

        while(p1):
            p1 = p1.next
            p2 = p2.next

        return p2


if __name__ == '__main__':
    ll1 = ll()
    ll1.insert_values([1,2,3,4])
    ll1.print(ll1.kth_to_last(2))





