import math

def merge(a, b):
    #print(a, b)
    a.append(math.inf)
    b.append(math.inf)
    index_a = 0
    index_b = 0
    result = []
    for i in range(len(a) - 1 + len(b) - 1):
        if a[index_a] < b[index_b]:
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1
    return result

def merge_sort(lower_end, upper_end, items):
    #print(lower_end, upper_end)
    if lower_end == upper_end:
        return [items[lower_end]]
    center = (lower_end + upper_end) // 2
    return merge(merge_sort(lower_end, center, items), merge_sort(center + 1, upper_end, items))

items = [3,2,9,15,7,8,1,41,12,4,14,16,12,20,2]
print(merge_sort(0, len(items) - 1, items))