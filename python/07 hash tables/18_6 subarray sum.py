def subarray_sum(numbers, target): 
    if len(numbers) == 0:
        return []

    for i in range(len(numbers) - 1):
        first_number = numbers[i]
        addition = first_number

        first_index = i
        last_index = -1
        if addition == target:
            last_index = i
            return [first_index, last_index]

        for j in range(i + 1, len(numbers)):   
            second_number = numbers[j]
            addition = addition + second_number

            if addition == target:
                last_index = j
                break

        if last_index >= first_index:
            return [first_index, last_index]
    
    return []


def subarray_sum_course(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


# nums = [1, 2, 3, 4, 5]
# target = 9
# print ( subarray_sum(nums, target) )

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

# nums = []
# target = 0
# print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
