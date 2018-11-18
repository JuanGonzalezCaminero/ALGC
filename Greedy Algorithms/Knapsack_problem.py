# Given a set of objects with a value V, and a weight W, and having a bag that can carry,
# at most, a weight Max_W, find a way to fill the bag maximizing the value of the objects
# inside, in this version, it is assumed we can take a fraction of each object and carry only
# that, having, of course, its value multiplied by the fraction as well
# The solution is a list of the objects we take and the fraction of each of them

#An object contains [Name, [Weight, Value]]
objects = [["pera", [1, 0.5]], ["patata", [1, 0.5]], ["tomate", [1, 0.5]],
           ["arena", [5, 5]], ["pescado", [3, 5]]]

# I determine the value per weight unit of each object
weight_per_unit = [a / b for a, b in zip([item[1][1] for item in objects],
                                         [item[1][0] for item in objects])]
#Adding the names
for i in zip(objects, weight_per_unit):
    i[0][1].append(i[1])

# Sort the values in descending order
objects = list(reversed(sorted(objects, key = lambda a: a[1][2])))
print(objects)

max_weight = 5
total_weight = 0
selected_objects = []

while total_weight != max_weight and len(objects) != 0:

    max_value_object = objects.pop(0)

    if total_weight + max_value_object[1][0] < max_weight:
        selected_objects.append((max_value_object, 1))
        total_weight += max_value_object[1][0]
    else:
        portion_to_take = (max_weight - total_weight) / max_value_object[1][0]
        selected_objects.append((max_value_object, portion_to_take))
        total_weight += max_value_object[1][0] * portion_to_take

print(selected_objects)
