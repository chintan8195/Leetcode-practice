# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head

        
# @lc code=end

