# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1=l1
        temp2=l2
        carry=0
        t=temp1.val+temp2.val
        v=t%10
        ans=ListNode(v)
        tt=ans
        carry=t//10
        temp1=temp1.next
        temp2=temp2.next
        while temp1!=None or temp2!=None:
            t=0
            if temp1!=None:
                t+=temp1.val
            if temp2!=None:
                t+=temp2.val
            t+=carry   
            v=t%10
            su=ListNode(v)
            tt.next=su
            tt=su
            carry=t//10
            if temp1!=None:
                temp1=temp1.next
            if temp2!=None:    
                temp2=temp2.next
        if carry!=0:        
            ne=ListNode(carry)
            tt.next=ne
        return ans    
        