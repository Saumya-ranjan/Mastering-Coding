# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1,l2):
        arr = []
        arr1 = []
        # Reverse the lists
        #L1
        prev , curr = None  , l1
        while curr!= None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #L2
        prev1 , curr1 = None  , l2
        while curr1!= None:
            nxt1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nxt1
        
        while prev!=None:
            arr.append(prev.val)
            prev = prev.next
        while prev1!=None:
            arr1.append(prev1.val)
            prev1 = prev1.next
        a = ""
        b = ""
        for i in arr1:
            a+=str(i)
        for j in arr:
            b+=str(j)
        c = str(int(a)+int(b))
        c = c[::-1]
        
        dummy = ListNode()
        tail = dummy
        count = 0
        while count!= len(c):
            tail.next = ListNode(c[count])
            tail = tail.next
            count+=1
        return dummy.next
         
    
            