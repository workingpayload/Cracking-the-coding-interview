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



    def iterator(self,node):
        list = []

        while(node):
            list.append(node.val)
            node = node.next

        return list




    def sumlist(self,node1,node2):
        list1 = self.iterator(node1)
        list2 = self.iterator(node2)
        st1=""
        st2 = ""
        for i in list1:
            st1+=str(i)
        for i in list2:
            st2+=str(i)
        new_sum = int(st1[::-1]) + int(st2[::-1])
        list3 = []
        for i in str(new_sum):
            list3.append(int(i))
        return list3


if __name__ == '__main__':
    ll1 = ll()
    ll2 = ll()
    ll3 = ll()
    ll4 = ll()
    ll1.insert_values([3,4,9,9])
    ll2.insert_values([2,7])
    list1 = ll1.sumlist(ll1.head,ll2.head)
    ll4.insert_values(list1[::-1])
    ll1.print(ll4.head)


def sumlist(node1,node2):
    list = []
    Q = 0
    while(node1 and node2):
        sum = node1.val + node2.val + Q
        if sum>9:
            list.append(int(str(sum)[-1]))
            Q = sum//10
        else:
            list.append(sum)
        node1 = node1.next
        node2 = node2.next

    while(Q>0):
        if node1:
            new_sum = node1.val+Q
            if new_sum>9:
                list.append(int(str(new_sum)[-1]))
                Q = sum // 10
            else:
                list.append(new_sum)
            node1 = node1.next

        elif node1:
            new_sum = node2.val+Q
            if new_sum>9:
                list.append(int(str(new_sum)[-1]))
                Q = sum // 10
            else:
                list.append(new_sum)
            node2 = node2.next
        else:
            list.append(Q)
            break

    while(node1):
        list.append(node1.val)
        node1 = node1.next
    while(node2):
        list.append(node2.val)
        node2 = node2.next

    ll3.insert_values(list)


sumlist(ll1.head,ll2.head)
ll3.print(ll3.head)
