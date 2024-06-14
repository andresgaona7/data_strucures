"""
Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.

Your function should return the new length of the list containing only unique elements. Note that you should not create a new 
list or use any additional data structures to solve this problem. The original list should be modified in-place.

!Constraints:
* The input list is sorted in non-decreasing order.
* The input list may contain duplicates.
* The function should have a time complexity of O(n), where n is the length of the input list.
* The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new 
* lists (this also means you cannot use a set like we did earlier in the course).
"""

def remove_duplicates(my_list):
    if len(my_list) == 0:
        return 0

    val = my_list[0]
    aux = 1
    for current in range(1, len(my_list)):
        if my_list[current] != val:
            val = my_list[current]
            my_list[aux] = val
            aux += 1

    return aux

def remove_duplicates_course(nums):
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    return write_pointer
    


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


