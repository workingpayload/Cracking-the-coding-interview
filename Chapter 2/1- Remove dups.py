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

    def removeduplicates(self):
        temp = self.head

        while(temp and temp.next):
            if temp.val == temp.next.val:
                    temp.next = temp.next.next
            else:
                    temp = temp.next


    def remove_dup_in_unsorted(self):
        seen = set()
        prev = None

        itr = self.head

        while(itr):
            if itr.val in seen:
                prev.next = itr.next
            else:
                seen.add(itr.val)
                prev = itr
            itr = itr.next

    def remove_from_unsorted_without_set(self):
        cur = self.head

        while(cur):
            run = cur
            while(run.next):
                if run.next.val==cur.val:
                    run.next = run.next.next
                else:
                    run = run.next
            cur = cur.next

if __name__ == '__main__':
    ll1 = ll()
    ll2 = ll()
    ll3 = ll()

    ll1.insert_values([1,1,2,2,3])
    ll2.insert_values([4,4,2,2,1,3,3])
    ll3.insert_values([4,4,2,2,1,3,3])
    ll1.removeduplicates()
    ll2.remove_dup_in_unsorted()
    ll3.remove_from_unsorted_without_set()
    ll1.print()
    ll2.print()
    ll3.print()
