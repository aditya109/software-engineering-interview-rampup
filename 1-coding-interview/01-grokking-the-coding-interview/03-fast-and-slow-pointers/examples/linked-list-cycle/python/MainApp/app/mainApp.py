# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MainApp:
    def __init__(self):
        pass

    '''
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
    following the nxt pointer. 
    Internally, pos is used to denote the index of the node that tail's nxt pointer is connected to. 
    Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
    
    Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    '''

    @staticmethod
    def run(head: ListNode) -> bool:
        """
        fast = head -> nxt
        slow = head

        fast += 2
        slow += 1


            👇👈👈👈👈👈👈
            👇        👆
        3 👉 2 👉 0 👉 4
                 ^
                 ^

        3 -> 2 -> None
        ^
            ^

        3 -> 2 -> None
        ^
            ^

        3 -> 2 -> None
        ^
            ^


        precondition:
        - fast pointer is not None - while loop
        - check - fast pointer != slow pointer
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
