class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)


class MainApp:
    def __init__(self):
        pass

    '''
    You are given the head of a singly linked-list. The list can be represented as:
    
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    
    Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
    
    Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
 
    '''

    @staticmethod
    def run(head):
        if not head or not head.next:
            return head
        slow = fast = head

        # find the middle
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse the second half
        reversed_slow = None
        while slow:
            temp = slow.next
            slow.next = reversed_slow
            reversed_slow = slow
            slow = temp

        head_front, head_back = head, reversed_slow

        while head_back.next:
            next_hop_front = head_front.next
            next_hop_back = head_back.next

            head_front.next = head_back
            head_back.next = next_hop_front

            head_back = next_hop_back
            head_front = next_hop_front
        return head

