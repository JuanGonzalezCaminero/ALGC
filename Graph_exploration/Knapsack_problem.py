import math
#[Peso, Valor]
objects = [[2, 3], [3, 5], [4, 6], [5, 10]]

#In this case we assume an unlimited number of objects of each type

def knapsack_backtracking(max_weight, node):
    max_value = node[1]

    for i in range(4):
        #Generate a child and explore it's next nodes
        if objects[i][0] + node[0] <= max_weight:
            max_value = max(max_value, knapsack_backtracking(max_weight, [objects[i][0] + node[0],
                                                                          objects[i][1] + node[1]]))

    return max_value


print("Result:", knapsack_backtracking(8, [0, 0]))

