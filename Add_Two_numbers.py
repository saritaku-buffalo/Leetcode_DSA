# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time complexity is O(MAX(m,n)) Where m is the length of l1 and n is the length of l2.
# space complexity is O(MAX(m,n) and O(1) extra space for variable carry

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = Listnode()  # create a dummy node to serve as the starting point of the result of linked list. 0 -> None
        curr = dummy # initialize a pointer to track the current node in result node
        carry = 0 # carry variable to track the any overflow from any digit additions.

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # V1 and v2 are the digits from the list l1 , l2 
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10 # the carry from previous addition
            val = val % 10 # will extract the unit digit of the sum to use as the digit in the result.
            curr.next = Listnode(val) # a ListNode created with val as its value and sets curr.next to this new node, linking to result list
            curr = curr.next # curr will move to the next new node which will be val -> None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next # return the head of the result list

        
