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




if __name__ == '__main__':
    ll1 = ll()
    ll1.insert_values([1,1,2,1])


def palindrome(node):
    stack = []
    fast = slow = node

    while(fast and fast.next):
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while(slow):
        top = stack[-1]
        stack.pop(-1)
        if top!=slow.val:
            return False
        slow = slow.next

    return True




print(palindrome(ll1.head))

