# Heaps in Python

## Min-Heap in Python

A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node. 

Mapping the elements of a heap into an array is trivial: if a node is stored at index k, then its left child is stored at index **2k + 1** and its right child at index **2k + 2**.

```
            5                      13
         /      \               /       \  
       10        15           16         31 
      /                      /  \        /  \
    30                     41    51    100   41
```

A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array. The root element will be at **Arr[0]**. For any i<sup>th</sup> node, i.e., **Arr[i]**:

- **Arr[(i -1) / 2]** returns its parent node.
- **Arr[(2 \* i) + 1]** returns its left child node.
- **Arr[(2 \* i) + 2]** returns its right child node.

**Operations on Min Heap :** 

1. **getMin()**: It returns the root element of Min Heap. Time Complexity of this operation is **O(1)**.
2. **extractMin()**: Removes the minimum element from MinHeap. Time Complexity of this Operation is **O(Log n)** as this operation needs to maintain the heap property (by calling heapify()) after removing root.
3. **insert()**: Inserting a new key takes **O(Log n)** time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

```python
from heapq import heapify, heappop, heappush

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")
 
element = heappop(heap)
 
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
```

```powershell
Head value of heap : 10
The heap elements : 
10 30 20 400 

The heap elements : 
20 30 400
```



## Max-Heap in Python

A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
Mapping the elements of a heap into an array is trivial: if a node is stored a index k, then its left child is stored at index **2k + 1** and its right child at index **2k + 2**.

![](https://media.geeksforgeeks.org/wp-content/uploads/MaxHeap.png)

**How is Max Heap is represented ?**
A Max Heap is a Complete Binary Tree. A Max heap is typically represented as an array. The root element will be at `Arr[0]`. Below table shows indexes of other nodes for the i<sup>th</sup> node, i.e.,` Arr[i]`:
`Arr[(i-1)/2]` Returns the parent node.
`Arr[(2*i)+1]` Returns the left child node.
`Arr[(2*i)+2]` Returns the right child node.

## Operations on Max Heap:

1. **getMax()**: It returns the root element of Max Heap. Time Complexity of this operation is **O(1)**.
2. **extractMax()**: Removes the maximum element from MaxHeap. Time Complexity of this Operation is **O(Log n)** as this operation needs to maintain the heap property (by calling heapify()) after removing root.
3. **insert()**: Inserting a new key takes **O(Log n)** time. We add a new key at the end of the tree. If new key is smaller than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

```python
from heapq import heappop, heappush, heapify
  
# Creating empty heap
heap = []
heapify(heap)
  
# Adding items to the heap using heappush
# function by multiplying them with -1
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)
  
# printing the value of maximum element
print("Head value of heap : "+str(-1 * heap[0]))
  
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-1 * i, end = ' ')
print("\n")
  
element = heappop(heap)
  
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-1 * i, end = ' ')
```

```powershell
Head value of heap : 400
The heap elements : 
400 30 20 10 

The heap elements : 
30 10 20 
```

