def first_non_repeating_char(string):
    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    for letter, counter in counts.items():
        if counter == 1:
            return letter
        
    return None

def first_non_repeating_char_course(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None


print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""