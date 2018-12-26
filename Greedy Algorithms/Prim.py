import math
import functools
nodes ={0,1,2,3,4,5}
tree_nodes = set()
tree_edges = []
edges = [([0, 1], 1), ([1, 2], 2), ([2, 3], 4), ([3, 4], 1), ([4, 5], 5), ([5, 0], 1),
         ([5, 1], 2), ([5, 2], 1), ([5, 3], 3)]
#Add the complementary of each edge
for i in range(len(edges)):
    edges.append(([edges[i][0][1], edges[i][0][0]], edges[i][1]))

def prim():
    initial = nodes.pop()
    nodes.add(initial)
    tree_nodes.add(initial)
    while len(tree_nodes) != len(nodes):
        min_cost = (None, math.inf)
        for i in range(len(edges)):
            if edges[i][0][0] in tree_nodes and edges[i][0][1] not in tree_nodes:
                if edges[i][1] < min_cost[1]:
                    min_cost = edges[i]
        tree_nodes.add(min_cost[0][1])
        tree_edges.append(min_cost)
    print(tree_nodes)
    print(tree_edges)

prim()