class ListNode:
    def __init__(self, val, successor=None):
        self.val = val
        self.next = successor


class MainApp:
    def __init__(self):
        pass

    '''
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:
    Input: head = [1,2]
    Output: [2,1]

    Example 3:
    Input: head = []
    Output: []
     
    '''
    """
    1 -> None              2 3 4 5 None

    """

    @staticmethod
    def run(head) -> ListNode:
        def reverse_iterative(node):
            reversed_head = None
            while node:
                t = node.next
                node.next = reversed_head
                reversed_head = node
                node = t
            return reversed_head

        def reverse_recursive(node, reversed_head):
            if node is None:
                return reversed_head
            temp = node.next
            node.next = reversed_head
            return reverse_recursive(temp, node)

        return reverse_recursive(head, None)


def print_list(temp):
    while temp:
        print("{0} -> ".format(temp.val), end="")
        temp = temp.next
    print("\n===============")

