def reverseList(head):

    current=head
    previous=None
    next=None

    while current:
        next=current.nextnode
        current.nextnode=previous
        previous=current
        current=next
    return previous