# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(head):
        dummy = ListNode()
        prev = None
        curr = head
        while curr!=None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    reverseList([1,2,3,4,5])
            