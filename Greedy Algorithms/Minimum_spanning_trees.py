# Let G = <N, A> be a Graph with N nodes and A Edges, let G' = <N, T> be a partial graph of
# that one, it must have, at least, N - 1 Edges to be connected.
# A Graph with N nodes with more than N - 1 Edges contains, at least, one cycle, so we can remove,
# at least, A - N - 1 edges in a graph with A edges and still have a connected graph (Removing edges
# that are part of a cycle, of course)
# G' is called the minimum spanning tree for G
# So, given a graph, find a minimum spanning tree with the least cost among it's edges (All edges have an
# Associated cost)

# Kruskal's solution
# In each step, choose the least-cost edge from the list of edges in G, if it doesn't form a cycle, add
# it to the solution, if it does, reject it and never consider it again
# selecting edges in this fashion will create groups of connected nodes that will eventually merge together
# to form the solution
# An edge forms a cycle if it does not add a new node to a group of connected elements, that is, an edge
# that connects two groups does not add new nodes to the solution, but is valid, an edge that does not
# connect two groups and adds no new nodes to the solution isn't
# We need:
# A list of candidates
# A list of selected elements

#Edge: 2-tuple with ([Node_1, Node_2], Cost), I assume the graph to not be directed so an edge goes both ways
edges = [([0, 1], 1), ([1, 2], 2), ([2, 3], 4), ([3, 4], 1), ([4, 5], 5), ([5, 0], 1),
         ([5, 1], 2), ([5, 2], 1), ([5, 3], 3)]
node_groups = [{0},{1},{2},{3},{4},{5}]
selected_edges = []
number_of_nodes = len(node_groups)
#Sort the edges in ascending order of cost
edges = sorted(edges, key = lambda a: a[1])

while len(selected_edges) != number_of_nodes - 1:
    #Pick the least-cost edge
    edge_to_check = edges[0]
    #Check that at least one new node is added or 2 groups
    #are connected
    group_1 = [a for a in node_groups if edge_to_check[0][0] in a]
    group_2 = [a for a in node_groups if edge_to_check[0][1] in a]
    if group_2 != group_1:
        print(node_groups)
        print(group_1)
        print(group_2)

        edges.pop(edges.index(edge_to_check))
        node_groups.pop(node_groups.index(group_1[0]))
        node_groups.pop(node_groups.index(group_2[0]))
        node_groups.append(group_1[0].union(group_2[0]))
        selected_edges.append(edge_to_check)
    else:
        edges.pop(edges.index(edge_to_check))
print(selected_edges)

















