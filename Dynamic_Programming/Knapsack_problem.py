import math
#[Peso, Valor]
objects = [[1, 1], [2, 6], [5, 18], [6, 22], [7, 28]]

def knapsack(max_weight):
    table = []
    for w in range(max_weight + 1):
        table.append([])
        #print(table)
        for object_index in range(len(objects)):
            #We have to fill in the first row element before anything else:

            #If the weight of the object is greater than the maximum allowed by the
            #knapsack, we can't do anything
            if object_index == 0 and objects[object_index][0] > w:
                table[w].append(0)
            elif object_index == 0:
                table[w].append(objects[object_index][1])
            elif objects[object_index][0] > w:
                table[w].append(table[w][object_index - 1])
            else:
                table[w].append(max(table[w][object_index - 1], objects[object_index][1] +
                                    table[w - objects[object_index][0]][object_index - 1]))

    for i in table:
        print(i)

    return table[max_weight][len(objects) - 1]

print("Result:", knapsack(11))