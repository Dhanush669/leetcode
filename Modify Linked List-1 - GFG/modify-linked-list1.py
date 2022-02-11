#User function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def modifyTheList(self, head):
        # Code here
        fast=head
        items=[]
        while fast!=None:
            items.append(fast.data)
            fast=fast.next
        if len(items)%2==0:    
            first=items[0:len(items)//2]
            last=items[len(items)//2:]
            last=last[::-1]
            items=items[::-1]
            for i in range(0,len(items)//2):
                items[i]=last[i]-first[i]
        else:
            first=items[0:len(items)//2]
            last=items[(len(items)//2)+1:]
            last=last[::-1]
            items=items[::-1]
            for i in range(0,len(items)//2):
                items[i]=last[i]-first[i]
        t=head        
        for i in items:
            t.data=i
            t=t.next
                
        #print(items)        
        return head
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().modifyTheList(lis.head)
        printList(newHead)

# } Driver Code Ends