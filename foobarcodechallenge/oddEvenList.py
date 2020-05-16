# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head) -> ListNode:
        cnt=0
        if not head or head.next == None: return head.val 
        odd=oddNode=ListNode()
        evenNode=even=ListNode()
        while(head):
            cnt+=1
            if(cnt%2!=0):
                oddNode.next=ListNode(head.val)
                oddNode=oddNode.next
                head=head.next
            else:
                evenNode.next=ListNode(head.val)
                evenNode=evenNode.next
                head=head.next
        oddNode.next=even.next
        return odd.next

