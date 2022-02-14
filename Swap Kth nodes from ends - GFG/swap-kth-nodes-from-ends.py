#User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
#Function to swap Kth node from beginning and end in a linked list.
def swapkthnode(head,num,k):
    # return head of new linked list
    #code here
    if k>num:
        return head
    if k==1:
        startNode=head
        end=num-k
        t=head
        #print(t.data,"bf")
        for i in range(1,end):
            t=t.next
        #print(t.data,"af")    
        endNode=t.next
        #print(t.data)
        t.next=startNode
        #enn=endNode.next
        endNode.next=startNode.next
        startNode.next=None
        head=endNode
        return head
        
    elif k==num:
        startNode=head
        t=head
        while t.next.next!=None:
            t=t.next
        endNode=t.next
        t.next=startNode
        endNode.next=startNode.next
        startNode.next=None
        return endNode
        
    else:
        t=head
        start=k-1
        end=num-k
        startNode=None
        endNode=None
        if end>start:
            for i in range(1,end):
                if i==start:
                    startNode=t
                t=t.next
            endNode=t.next
            t.next=startNode.next
            snn=startNode.next
            startNode.next=endNode
            #csnn=snn
            snn.next=endNode.next
            endNode.next=t
            return head
            
            
        else:
            for i in range(1,start):
                if i==end:
                    endNode=t
                t=t.next  
            #print(t.data)    
            startNode=t.next
            t.next=endNode.next
            endNode.next=startNode
            snn=startNode.next
            startNode.next=t.next.next
            t.next.next=snn
            return head    
        
        
           

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head=swapkthnode(a.head,n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends