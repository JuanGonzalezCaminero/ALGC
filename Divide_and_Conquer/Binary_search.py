import math
#Given a sorted array and an item x, find x in the array, or, if it is not there,
#find the index where it should be inserted
items = [1,2,3,5,7,8,9,10,12,13,14,16,17,20,22]
item_to_find = 23

#[lower_end, upper_end)
def binary_search(lower_end, upper_end, items, item_to_find):
    print(lower_end, upper_end)
    if lower_end == upper_end:
        if items[lower_end] < item_to_find:
            return lower_end + 1
        return lower_end
    #Compute the index in the middle of the array:
    center = (upper_end + lower_end) // 2
    if item_to_find <= items[center]:
        return binary_search(lower_end, center, items, item_to_find)
    else:
        return binary_search(center + 1, upper_end, items, item_to_find)

print(binary_search(0, len(items), items, item_to_find))