class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def shift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:


