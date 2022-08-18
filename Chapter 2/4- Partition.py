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

    def partition(self,node,x):
        head = tail = node

        while(node):
            next = node.next

            if node.val<=x:
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node

            node = next
        tail.next = None

        return head


if __name__ == '__main__':
    ll1 = ll()
    ll1.insert_values([9,3,1,3,4])
    ll1.print(ll1.partition(ll1.head,3))
