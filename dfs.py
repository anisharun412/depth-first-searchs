'''
Depth First Search uses STACK AND RECURSION
'''

from collections import defaultdict

def depth_first_search(graph, current_node, visited_nodes, traversal_order):
    traversal_order.append(current_node)
    visited_nodes[current_node] = True

    for neighbor in graph[current_node]:
        if not visited_nodes[neighbor]:
            depth_first_search(graph, neighbor, visited_nodes, traversal_order)

    return traversal_order

graph = defaultdict(list)
number_of_nodes, number_of_edges = map(int, input().split())

for _ in range(number_of_edges):
    node_1, node_2 = input().split()
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

start_node = input()
visited_nodes = defaultdict(bool)
traversal_order = []
result = depth_first_search(graph, start_node, visited_nodes, traversal_order)

print(result)
