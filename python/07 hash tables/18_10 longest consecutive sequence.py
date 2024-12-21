def longest_consecutive_sequence(nums):
    my_set = set()
    longest = 0
    for num in nums:
        cont = 1
        aux = num

        while True:
            aux = aux + 1
            if aux in nums:
                cont += 1
            else:
                break

        longest = max(longest, cont)

    return longest


def longest_consecutive_sequence_course(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""