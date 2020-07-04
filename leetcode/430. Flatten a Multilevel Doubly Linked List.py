
""" 
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
            1
            |
            2
            |
            3
          / |
         7  4
         |  |
         8  5
       / |  |
      11 9  6
      |  |
     12  10
 """
 # Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head): 
        if not head:
            return head
        temp = Node(None,None,head, None)
        self.flatten_dfs(temp,head)
        temp.next.prev = None
        return temp.next
    
    def flatten_dfs(self,prev,curr):
        if not curr:
            return prev
        curr.prev = prev
        prev.next = curr
        next_ = curr.next
        tail = self.flatten_dfs(curr,curr.child)
        curr.child = None
        return self.flatten_dfs(tail,next_)

# Iterative
class Solution(object):
    def flatten(self, head):
        if not head:
            return
        
        dummy = Node(0,None,head,None)     
        stack = []
        stack.append(head)
        prev = dummy
        
        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root
            
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        
            
        
        dummy.next.prev = None
        return dummy.next