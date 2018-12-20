import math
graph = [[0, 5, math.inf, math.inf],
         [50, 0, 15, 5],
         [30, math.inf, 0, 15],
         [15, math.inf, 5, 0]]

for row in graph:
    for char in row:
        if char == math.inf:
            print("∞".rjust(2), end = " ")
        else:
            print(str(char).rjust(2), end=" ")
    print()

def floyd(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd(graph)
print("-------------------------")
for row in graph:
    for char in row:
        if char == math.inf:
            print("∞".rjust(2), end = " ")
        else:
            print(str(char).rjust(2), end=" ")
    print()
