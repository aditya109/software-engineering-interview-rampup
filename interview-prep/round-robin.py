from collections import defaultdict
from queue import Queue


def provide_round_robin_scheduling(processes, time_quanta):

    # make a process dict
    # mapping schema: arrival_time : [(id, burst_time)]
    process_map = defaultdict(list)

    for (pid, at, bt) in processes:
        process_map[at].append((pid, bt))
    """
    1 :0 5
    2 :1 4
    3 :2 2
    4 :4 1
4 
1 0 5
2 1 4
3 2 2
4 4 1    
    """
    print(process_map)
    arrival_times = list(process_map.keys())
    # we have all unique arrival times sorted in descending order
    arrival_times.sort(reverse=True)

    # 4 2 1 0
    # this is our cpu time
    t = 0

    ready_queue = Queue()
    # stores our final answer
    final_queue = []
    top_pid, top_bt = float("-inf"), float("-inf")
    current_time = arrival_times.pop()
    # iterate till arrival_times is empty
    while len(arrival_times) > 0:
        # we get the lowest arrival time
        # 0
        print("Arrival times = ", end="")
        print(arrival_times)
        print("Current Time = {0}, Time = {1}".format(current_time, t))
        if current_time <= t:
            # add process[current_time] to queue
            for (pid, bt) in process_map[current_time]:
                # all the fresh processes will be added to last of the queue
                ready_queue.put((pid, bt))
                print("queue = ", end="")
                for n in list(ready_queue.queue):
                    print(n, end=" ")
                print()
            # get the next arrival_times in queue
            current_time = arrival_times.pop()
            continue
        print("top_pid = {0}, top_bt = {1}".format(top_pid, top_bt))
        if top_pid != float("inf") and top_bt != float("inf") and top_bt > 0:
            ready_queue.put((top_pid, top_bt))
            print("queue = ", end="")
            for n in list(ready_queue.queue):
                print(n, end=" ")
            print()
        inc = 0
        if not ready_queue.empty():
            print("queue = ", end="")
            for n in list(ready_queue.queue):
                print(n, end=" ")
            print()
            (top_pid, top_bt) = ready_queue.get()
            final_queue.append(top_pid)
            print("Final Queue = ", end="")
            inc = min(time_quanta, top_bt)
            top_bt -= inc

        print(final_queue)
        print("\n===================")
        t += inc

    while not ready_queue.empty():
        (top_pid, top_bt) = ready_queue.get()
        final_queue.append(top_pid)
        inc = min(time_quanta, top_bt)
        top_bt -= inc
        if top_bt > 0:
            ready_queue.put((top_pid, top_bt))
    return final_queue


"""
cuurent_time = 2
t= 1
4   
q = (1, 3) (2, 4)

[1  

id arrival_time burst_time

4 
1 0 5
2 1 4
3 2 2
4 4 1
"""


number_of_processes = int(input())
process_entries = []
for i in range(number_of_processes):
    process_entry = input().split(" ")
    pid, at, bt = int(process_entry[0]), int(
        process_entry[1]), int(process_entry[2])
    process_entries.append((pid, at, bt))
res = provide_round_robin_scheduling(process_entries, 2)
print(res)
