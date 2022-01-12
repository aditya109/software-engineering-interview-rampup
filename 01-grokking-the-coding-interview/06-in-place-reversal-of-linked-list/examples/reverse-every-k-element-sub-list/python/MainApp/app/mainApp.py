class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(node):
    if node is None:
        print("\n===================")
        return
    print("{0} -> ".format(node.val), end="")
    print_list(node.next)


class MainApp:
    def __init__(self):
        pass

    '''
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    
    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    
    Follow up:
    
    Could you solve the problem in O(1) extra memory space?
    You may not alter the values in the list's nodes, only nodes itself may be changed.
     
    
    Example 1:
    
    
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    Example 2:
    
    
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    Example 3:
    
    Input: head = [1,2,3,4,5], k = 1
    Output: [1,2,3,4,5]
    Example 4:
    
    Input: head = [1], k = 1
    Output: [1]
 
    '''

    def get_list_length(self, node, length=0):
        if node is None:
            return length
        return self.get_list_length(node.next, length + 1)

    def run(self, head, k):
        """
        |1| -> 2 -> 3 -> 4 -> 5 -> None
        2 -> 1 -> 4 -> 3
        """
        if head is None or k == 1:
            return head
        length = self.get_list_length(head, 0)
        prev = None
        curr = head
        while length >= k:
            tail = curr
            connection = prev
            temp = k
            while temp > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                temp -= 1
            if connection is not None:
                connection.next = prev
            else:
                head = prev
            prev = tail
            tail.next = curr
            length -= k
        return head


def is_equal(a, b):
    while a and b:
        if a.val != b.val:
            return False
        a = a.next
        b = b.next
    return True


