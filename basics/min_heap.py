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