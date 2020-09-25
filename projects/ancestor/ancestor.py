from collections import deque, defaultdict

def earliest_ancestor(ancestors, starting_node):
    # clue is in child pair with no parent being the earliest ancestor
    # similar to dest city problem covered in lecture 2!
    pass


def create_graph(edges):
    # every key I add to to this dict, will have a default value of set()
    graph = defaultdict(set)

    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)

    return graph


arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(arr, 1)) # 10
print(earliest_ancestor(arr, 2)) # -1
print(earliest_ancestor(arr, 3)) # 10
print(earliest_ancestor(arr, 4)) # -1
print(earliest_ancestor(arr, 5)) # 4
print(earliest_ancestor(arr, 6)) # 10
print(earliest_ancestor(arr, 7)) # 4
print(earliest_ancestor(arr, 8)) # 4
print(earliest_ancestor(arr, 9)) # 4
print(earliest_ancestor(arr, 10)) # -1
print(earliest_ancestor(arr, 11)) # -1