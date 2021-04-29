class ListNode:
    def __init__(self, val, successor=None):
        self.val = val
        self.next = successor


def print_list(node):
    if node is None:
        print("\n===================")
        return
    print("{0} -> ".format(node.val), end="")
    print_list(node.next)


def reverse_list(node, reversed_head=None) -> ListNode:
    if node is None:
        return reversed_head
    t = node.next
    node.next = reversed_head
    return reverse_list(t, node)


class MainApp:
    def __init__(self):
        pass

    '''
    Given the head of a singly linked list and two integers left and right where left <= right, 
    reverse the nodes of the list from position left to position right, and return the reversed list.
    
    Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

    Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]
 
    '''

    @staticmethod
    def run(head, left, right):
        """
        1   2   3   4   5
        ^
        1   4   3   2   5


        """
        if head is None or left == right:
            return head

        prev = None
        curr = head

        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1

        connection = prev  # 1->
        tail = curr

        while right > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            right -= 1
        if connection is not None:
            connection.next = prev
        else:
            head = prev
        tail.next = curr
        return head
