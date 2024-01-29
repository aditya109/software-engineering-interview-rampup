from collections import defaultdict
from queue import Queue


def provide_round_robin_scheduling(processes, time_quanta):
    process_map = defaultdict(list)
    INF = float("-inf")
    for (pid, at, bt) in processes:
        process_map[at].append((pid, bt))

    print(process_map)

    arrival_times = list(process_map.keys())
    arrival_times.sort(reverse=True)

    top_pid, top_bt = INF, INF
    current_time = arrival_times.pop()
    ready_queue = Queue()
    final_queue = []
    t = 0

    while True:
        if current_time <= t:
            for pid, bt in process_map[current_time]:
                ready_queue.put((pid, bt))
                print("queue = ", end="")
                for n in list(ready_queue.queue):
                    print(n, end=" ")
                print()
            
            if len(arrival_times) != 0:
                current_time = arrival_times.pop()
                continue
            else:
                break
            # print("queue = ", end="")
            # for n in list(ready_queue.queue):
            #     print(n, end=" ")
            # print()

        inc = -1
        if not ready_queue.empty():
            print(top_pid, top_bt)
            if top_pid != INF and top_bt != INF and top_bt > 0:
                ready_queue.put((top_pid, top_bt))
            print("queue = ", end="")
            for n in list(ready_queue.queue):
                print(n, end=" ")
            print()
            (top_pid, top_bt) = ready_queue.get()
            inc = min(time_quanta, top_bt)
            top_bt -= inc
            final_queue.append(top_pid)
            print(final_queue)
            print("queue = ", end="")
            for n in list(ready_queue.queue):
                print(n, end=" ")
            print()
        t += inc
        print("\n==================")

    while not ready_queue.empty():
        (top_pid, top_bt) = ready_queue.get()
        inc = min(time_quanta, top_bt)
        top_bt -= inc
        final_queue.append(top_pid)
        print(final_queue)
        print("queue = ", end="")
        for n in list(ready_queue.queue):
            print(n, end=" ")
        print()


s = [
    (1, 0, 5),
    (2, 1, 4),
    (3, 2, 2),
    (4, 4, 1)
]
tq = 2

res = provide_round_robin_scheduling(s, 2)
print(res)
