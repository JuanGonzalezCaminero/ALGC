
#[lower, upper]
def quicksort(lower_end, upper_end, items):
    center = (lower_end + upper_end) // 2
    pivot = items[lower_end]
    index_up = lower_end
    index_down = upper_end + 1

    if lower_end == upper_end:
        return

    #We need to make a first move on the indexes to their first swap
    #indexes, as the first step in the loop is the swap, also, in case the items are
    #already in the correct order
    while True:
        index_up += 1
        if items[index_up] > pivot or index_up >= upper_end:
            break
    while True:
        index_down -= 1
        #No need to check if it's below the lower end because it will stop at the pivot anyway
        if items[index_down] <= pivot:
            break

    while index_up < index_down:
        #print("Swap:", items[index_up], items[index_down])
        # Swap the elements
        temp = items[index_up]
        items[index_up] = items[index_down]
        items[index_down] = temp

        while items[index_up] <= pivot:
            index_up += 1
        while items[index_down] > pivot:
            index_down -= 1

    #Swap the pivot with the descending index
    temp = items[lower_end]
    items[lower_end] = items[index_down]
    items[index_down] = temp

    print(items)

    quicksort(lower_end, center, items)
    quicksort(center + 1, upper_end, items)

items = [4,3,2,1]
#items = [4,8,5,7,2,1,6,3,4,6,1,1,2,10,20,3,1,67,3,2,7,5,4,3,9]

quicksort(0, len(items) - 1, items)
print(items)