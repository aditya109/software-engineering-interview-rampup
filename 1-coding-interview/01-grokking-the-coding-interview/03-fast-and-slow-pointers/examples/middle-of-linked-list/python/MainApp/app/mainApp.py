class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MainApp:
    def __init__(self):
        pass

    '''
    Given a non-empty, singly linked list with head node head, return a middle node of linked list.
    If there are two middle nodes, return the second middle node.
    Example 1:
    
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.nxt.val = 4, ans.nxt.nxt.val = 5, and ans.nxt.nxt.nxt = NULL.
    
    Example 2:
    
    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4, we return the second one.
    '''

    @staticmethod
    def run(head):
        slow = fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow.val
