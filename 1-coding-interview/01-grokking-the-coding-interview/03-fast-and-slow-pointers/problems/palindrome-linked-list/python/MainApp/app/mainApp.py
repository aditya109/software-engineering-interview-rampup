class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self) -> str:
        return str(self.val) + " -> " + str(self.next)


class MainApp:
    def __init__(self):
        pass

    '''
    Given the head of a singly linked list, return true if it is a palindrome.
    
    Example 1:
    
    Input: head = [1,2,2,1]
    Output: true
    Example 2:
    
    Input: head = [1,2,1]
    Output: false
     
    '''
    '''
    1 -> 2 -> 2 -> 1 -> None
              s^   n^
                        f^        
    '''
    @staticmethod
    def run(head):
        fast = slow = head

        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        # compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
