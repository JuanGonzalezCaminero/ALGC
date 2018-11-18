# Let G = <N, A> be a directed graph with weighted edges, given a node from G, find the
# length of the shortest path to each node from there

#Node: A List with [name, distant_to_source]
#Edge: 2-tuple with ([Node_1, Node_2], Cost)
edges = [(['A', 'B'], 1), (['A', 'C'], 1), (['A', 'D'], 1), (['G', 'D'], 1), (['D', 'E'], 2), (['E', 'X'], 3),
         (['E', 'F'], 3), (['X', 'F'], 3)]
nodes = [['A', None], ['B', None], ['C', None], ['D', None], ['E', None], ['F', None], ['G', None], ['X', None]]

source = 'A'

selected_nodes = []

for i in nodes:
    if i[0] == source:
        selected_nodes.append(nodes.pop(nodes.index([source, None])))
        selected_nodes[0][1] = 0

candidate_nodes = nodes

while len(candidate_nodes) != 0:
    #Pick a node that is connected to one of the already selected nodes
    for i in candidate_nodes:
        node_to_check = i
        if