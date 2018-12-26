#Given a set of n elements, find the i-th smallest element
#In this implementation we assume all elements are different

items = [9,11,4,7,1,8,15,10,3,6,2,13,12]
print(items)
def selection(items, start, end, target):
    pivot = items[start]
    index_ascending = start
    index_descending = end + 1
    #Find the first elements to swap
    while True:
        index_ascending += 1
        if items[index_ascending] > pivot or index_ascending >= end:
            break
    while True:
        index_descending -= 1
        if items[index_descending] <= pivot:
            break

    #Continue until all elements are ordered
    while index_ascending < index_descending:
        #print("Swap:", items[index_ascending], items[index_descending])
        #print(items)
        #Swap the elements
        temp = items[index_ascending]
        items[index_ascending] = items[index_descending]
        items[index_descending] = temp
        #Increase
        while True:
            index_ascending += 1
            if items[index_ascending] > pivot or index_ascending >= end:
                break
        while True:
            index_descending -= 1
            if items[index_descending] <= pivot:
                break
    #Lastly, swap the descending index with the pivot
    temp = items[index_descending]
    items[index_descending] = items[start]
    items[start] = temp

    #Call the algorithm again on the half of the array where the desired element is
    if target < items.index(pivot):
        return(selection(items, start, items.index(pivot) - 1, target))
    elif target > items.index(pivot):
        return(selection(items, items.index(pivot) + 1, end, target))
    else:
        return pivot

print(selection(items, 0, len(items) - 1, 7))















