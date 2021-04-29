from collections import defaultdict


class MainApp:
    def __init__(self):
        pass

    '''
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
    Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
    
    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: true
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
    before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
    
    Example 2:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: false
    Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
    
    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: true
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
    '''

    @staticmethod
    def run(req, tasks):
        # turn req into req_graph
        req_graph = defaultdict(list)
        for (target, dependency) in req:
            req_graph[target].append(dependency)
            if dependency not in req_graph:
                req_graph[dependency] = []




print(MainApp().run(req=[
    (0, 1),
    (1, 2),
    (2, 0)
], tasks=3))
print("\n====================")
print(MainApp().run(req=[
    (0, 1),
    (1, 2)
], tasks=3))
print("\n====================")

print(MainApp().run(req=[
    (2, 5),
    (0, 5),
    (0, 4),
    (1, 4),
    (3, 2),
    (1, 3)
], tasks=3))

# def detect_cycle(req):
#     # turn req into req_graph
#     req_graph = defaultdict(list)
#     for (target, dependency) in req:
#         req_graph[target].append(dependency)
#         if dependency not in req_graph:
#             req_graph[dependency] = []
#
#     def dfs(graph, start, visited=set()):
#         if start not in visited:
#             visited.add(start)
#             for neighbour in graph[start]:
#                 if neighbour in visited:
#                     return False
#                 return dfs(graph, neighbour, visited)
#         return True
#
#     for node in req_graph:
#         print(dfs(req_graph, node, set()))
#         break
#
#
# req = [
#     (0, 1),
#     (1, 2)
# ]
# detect_cycle(req)
#
#
# req = [
#     (0, 1),
#     (1, 2),
#     (2, 0)
# ]
# detect_cycle(req)
