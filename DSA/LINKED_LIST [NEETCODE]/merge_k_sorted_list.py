# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(lists):
        
        # Create an array so that u can store each element of linkedlist inside it:
        arr= []
        for head in lists:
            curr = head
            while curr!=None:
                arr.append(curr.val)
                curr = curr.next
                
        # Sort the array and add it in new linkedlist
        a = ListNode()
        dummy = a
        arr.sort()
        for i in range(len(arr)):
            dummy.next = ListNode(arr[i])
            dummy = dummy.next
        return a.next
                
            
        