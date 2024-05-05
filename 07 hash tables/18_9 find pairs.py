def find_pairs(arr1, arr2, target):
    outs = []
    for num1 in arr1:
        diff = target - num1
        if diff in arr2:
            outs.append((num1, diff))

    return outs




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""