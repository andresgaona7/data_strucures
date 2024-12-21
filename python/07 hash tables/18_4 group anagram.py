def group_anagrams(strings):
    database = {}
    for word in strings:
        database[word] = False

    anagrams = []
    for i in range(len(strings)):
        current_word = strings[i]

        if database[current_word]:
            continue

        # Gets the letters in a word
        letters = {}
        for letter in current_word:
            if letter not in letters:
                letters[letter] = True

        # Compare words
        current_word_anagrams = []
        for j in range(i, len(strings)):
            next_word = strings[j]

            # Check if the next_word is an anagram of current_word
            is_anagram = True
            for letter in next_word:
                if letter not in current_word:
                    is_anagram = False
                    break

            if is_anagram:
                database[next_word] = True
                current_word_anagrams.append(next_word)
    
        anagrams.append(current_word_anagrams)

    return anagrams


def group_anagrams_course(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""