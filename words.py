"""
1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
2. Turn that into a function,***print_upper_words***. Test it out. 
3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters. 
    For example:
    # this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
"""


def print_upper_words(words, set_of_letters):
    list = []
    # Go through every word of words and each letter in the set of letters
    for word in words:
        for letter in set_of_letters:
            # Append capitalized word if the first letter of every word is equal to the letter in set_of_letters
            if word.startswith(letter):
                list.append(word.upper())
    # Print each item of the list in seperate lines
    print(*list, sep="\n")


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})
