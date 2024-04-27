def iterative_solution(head):
    prev, cur_node = None, head
    while cur_node:
        nxt = cur_node.next
        cur_node.next, prev, cur_node = prev, cur_node, nxt
    return prev


def recursive_solution(head):
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = recursive_solution(head.next)
        head.next.next = head
    head.next = None
    return newHead
