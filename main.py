# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    # to remove spaces in between the strings
    word = word.replace(" ", "")
    anagram = anagram.lower()
    # to remove spaces in between the strings
    anagram = anagram.replace(" ", "")
    print(anagram)

    # checking the

    if (sorted(word) != sorted(anagram)):
            return False
    else:
        return True


print(find_anagram('h ello', 'l hoel'))
