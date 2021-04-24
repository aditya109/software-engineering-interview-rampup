# Linked List - Reversal

If a linked list is `a -> b -> c -> d`, we want to reverse the list `d -> c -> b -> a`.

Basically we are reversing the direction of the node.

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self) -> str:
        return str(self.val) + " -> " + str(self.next)


node_3 = ListNode(3)
node_2 = ListNode(2)
node_0 = ListNode(0)
node_neg4 = ListNode(-4)

node_3.next = node_2
node_2.next = node_0
node_0.next = node_neg4
node_neg4.next = None

print(node_3)

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    while head:
        temp_next = head.next
        head.next = prev
        prev = head
        head = temp_next
    return prev


print(reverse_linked_list(node_3))
```

```powershell
3 -> 2 -> 0 -> -4 -> None
-4 -> 0 -> 2 -> 3 -> None
```

