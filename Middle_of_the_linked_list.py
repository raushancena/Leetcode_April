# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s=0
        b=head
        while(b!=None):
            s=s+1
            b=b.next
        c=s/2
        c1=int(c)
        if(c!=c1):
            c1=c1+1
        a=head
        p=0
        while(a!=None):
            if(p>=c1-1 and s%2!=0):
                return a
            elif(p>=c1 and s%2==0):
                return a
            a=a.next
            p=p+1
            #return l