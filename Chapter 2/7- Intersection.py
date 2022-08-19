# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lena = 0
        lenb = 0
        tempA = headA
        tempB = headB
        
        while(headA.next):
            headA = headA.next
            lena+=1
            
        while(headB.next):
            headB = headB.next
            lenb+=1
            
        if headA!=headB:
            return 
        
        dif = 0
        
        if lena>lenb:
            dif = (lena+1)-(lenb+1)
            
            while(dif):
                tempA = tempA.next
                dif-=1
            
        else:
            dif = (lenb+1)-(lena+1)
            
            while(dif):
                tempB = tempB.next
                dif-=1
            
            
            
        while(tempA and tempB):
            if tempA==tempB:
                return tempA
            else:
                tempA=tempA.next
                tempB=tempB.next
                            
