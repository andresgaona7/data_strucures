"""
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an 
integer k as input and rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

!Constraints:
* Each element of the input list is an integer.
* The integer k is non-negative.
"""

def rotate(nums, k):
    for _ in range(k):
        temp = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp

def rotate_course(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""