# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None # Initially set head, prev,temp as EmptyNode
        prev = None
        temp = None
        carry = 0 # Set carry as 0
        while (l1 is not None or l2 is not None): # Keep looping until If both ListNode l1 and l2 are not empty
            fdigit = 0 if l1 is None else l1.val # If ListNode l1 empty, then return 0 otherwise whatever value in l1 will return
            sdigit = 0 if l2 is None else l2.val # Same explain above for l2
            sumdigit = carry + fdigit + sdigit # Add both ListNode l1 and l2 listwise
            
            carry = 1 if sumdigit > 9 else 0 # If the value exceed 9, then carry is generated as 1, otherwise 0
            
            sumdigit = sumdigit if sumdigit < 10 else sumdigit % 10 # If sumdigit less than 10 then return whatever it was, otherwise take modulas 10
            
            temp = ListNode(sumdigit) # Store sumDigit in temp ListNode
            
            if head is None: # If head is empty, set head to temp
                head = temp
            else:
                prev.next = temp
                
            prev = temp # set previous value as temp ListNode
            
            if l1 is not None: # Move on to the next element in l1 if it is not None
                l1 = l1.next
            if l2 is not None: # Same explain above for l2
                l2 = l2.next
        
        if carry > 0: # After addition over, If final carry is 1, set value to next value of temp
            temp.next = ListNode(carry)
            
        return head
