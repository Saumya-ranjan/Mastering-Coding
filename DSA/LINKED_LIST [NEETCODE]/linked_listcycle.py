# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        hashes = set()
        while head:  
            hh = hash(head) 
            print(hh)
            if hh in hashes:
                return True
            else:
                hashes.add(hh)
            head = head.next
        return False
a = Solution.hasCycle([3,2,0,-4])
print(a)
    

# FLOYD [Tortoise and Hare]   
#    
#         slow = head
#         fast = head
#         while fast!= None and fast.next!= None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True 
            
#         return False
            