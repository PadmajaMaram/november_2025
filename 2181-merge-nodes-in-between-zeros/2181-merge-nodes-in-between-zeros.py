# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        vals=[]
        curr=head.next
        total=0
        while curr:
            if curr.val==0:
                vals.append(total)
                total=0
            else:
                total+=curr.val
            curr=curr.next
        dummy=ListNode(0)
        temp=dummy
        for x in vals:
            temp.next=ListNode(x)
            temp=temp.next
        return dummy.next
        

