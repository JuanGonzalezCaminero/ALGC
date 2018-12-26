items = [1,2,3,5,6,7,9,11,12,13,15,18,20]


def binary_search(start, end, target, items):
    center = (start + end)//2
    if start == end:
        if target == items[start] and target - 1 == start:
            return True
        else:
            return False

    if items[center] < target:
        return binary_search(center + 1, end, target, items)
    elif items[center] >= target:
        return binary_search(start, center, target, items)

print(binary_search(0, len(items) - 1, 5, items))