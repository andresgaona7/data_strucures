"""
Write a Python function called find_longest_string that takes a list of strings as an input and 
returns the longest string in the list. The function should iterate through each string in the list, 
check its length, and keep track of the longest string seen so far. Once it has looped through all the 
strings, the function should return the longest string found.
"""

def find_longest_string(my_list):
    longest_string = ''
    max_length = None

    for i in range(len(my_list)):
        if i == 0 :
            longest_string = my_list[i]
            max_length = len(my_list[i])
        else:
            if len(my_list[i]) > max_length:
                longest_string = my_list[i]
                max_length = len(my_list[i])

    return longest_string

def find_longest_string_course(string_list):
    longest_string = ""
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


string_list = ['hello', 'hola']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""