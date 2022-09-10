# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(head):
        
        # Find the Middle:
        # Floyd hare and tortoise:
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the second part of the Linkedlist
        second = slow.next
        curr = second
        prev = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        second = prev
            
        # Finding First Part:
        slow.next = None 
        first = head
        
        # Merging 1st and second Linkedlist to Go for the solution
        a = ListNode()
        dummy = a
        count = 0
        while second:
            if count%2 == 0:
                dummy.next = first
                first = first.next
            else:
                dummy.next = second
                second = second.next
            dummy = dummy.next
            count+=1
        if first!=None:
            dummy.next = first
        return a.next
                