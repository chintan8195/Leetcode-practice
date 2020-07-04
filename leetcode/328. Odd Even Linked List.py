def oddEvenList(head):
    if not head or not head.next:
        return head
    
    p1 = head
    p2 = head.next
    pre = p2
    while p2 and p2.next: 
        p1.next = p2.next
        p1 = p1.next
        p2.next = p1.next
        p2 = p2.next
    p1.next = pre
    return head