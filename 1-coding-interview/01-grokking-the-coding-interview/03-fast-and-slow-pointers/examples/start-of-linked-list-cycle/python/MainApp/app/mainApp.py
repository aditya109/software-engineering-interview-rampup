class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return str(self.val) + " -> "


class MainApp:
    def __init__(self):
        pass

    '''
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
    following the nxt pointer. 
    Internally, pos is used to denote the index of the node that tail's nxt pointer is connected to. 
    Note that pos is not passed as a parameter.
    
    Notice that you should not modify the linked list.
    
    Example 1:
    
    
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    Example 2:
    
    
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    Example 3:
    
    
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.
 
    '''

    @staticmethod
    def run(head) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow.val
        return None
