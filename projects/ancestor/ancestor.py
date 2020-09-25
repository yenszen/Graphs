from collections import deque, defaultdict

def earliest_ancestor(ancestors, starting_node):
    # clue is in child pair with no parent being the earliest ancestor
    # similar to dest city problem covered in lecture 2!
    graph = create_graph(ancestors)
    stack = deque()
    stack.append((starting_node, 0)) # node, distance from starting_node
    visited = set()
    earliestAncestor = (starting_node, 0)

    while len(stack) > 0:
        current = stack.pop() # (current_node, distance from starting_node)
        current_node, distance = current[0], current[1]
        visited.add(current)

        if current_node not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = current
            elif distance == earliestAncestor[1] and current_node < earliestAncestor[0]:
                earliestAncestor = current
        else:
            for ancestor in graph[current_node]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def create_graph(edges):
    # every key I add to to this dict, will have a default value of set()
    graph = defaultdict(set)

    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)

    return graph


# arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(arr, 1)) # 10
# print(earliest_ancestor(arr, 2)) # -1
# print(earliest_ancestor(arr, 3)) # 10
# print(earliest_ancestor(arr, 4)) # -1
# print(earliest_ancestor(arr, 5)) # 4
# print(earliest_ancestor(arr, 6)) # 10
# print(earliest_ancestor(arr, 7)) # 4
# print(earliest_ancestor(arr, 8)) # 4
# print(earliest_ancestor(arr, 9)) # 4
# print(earliest_ancestor(arr, 10)) # -1
# print(earliest_ancestor(arr, 11)) # -1