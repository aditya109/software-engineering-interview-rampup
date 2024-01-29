class MainApp:
    def __init__(self):
        pass

    '''
    Problem Statement
    '''

    @staticmethod
    def run(graph, start):
        visited = set()
        top_sorted_nodes = list()

        def dfs(graph, start):
            if start not in visited:
                visited.add(start)
                for neighbour in graph[start]:
                    dfs(graph, neighbour)
                top_sorted_nodes.insert(0, start)

        for node in graph:
            dfs(graph, node)

        # for node in top_sorted_nodes:
        #     print("{0} -> ".format(node), end="")
        return top_sorted_nodes
