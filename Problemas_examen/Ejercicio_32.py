import math
graph = [[0, 2, 5, 10, 15],
         [math.inf, 0, 2, 3, 5],
         [math.inf, math.inf, 0, 2, 7],
         [math.inf, math.inf, math.inf, 0, 2],
         [math.inf, math.inf, math.inf, math.inf, 0]]

for row in graph:
    for char in row:
        if char == math.inf:
            print("∞".rjust(2), end = " ")
        else:
            print(str(char).rjust(2), end=" ")
    print()

for intermediate_node in range(0, len(graph)):
    for origin in range(0, len(graph)):
        for destiny in range(0, len(graph)):
            graph[origin][destiny] = min(graph[origin][destiny],
                                         graph[origin][intermediate_node] +
                                         graph[intermediate_node][destiny])

print("-------------------------")
for row in graph:
    for char in row:
        if char == math.inf:
            print("∞".rjust(2), end = " ")
        else:
            print(str(char).rjust(2), end=" ")
    print()