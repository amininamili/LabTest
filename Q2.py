string = "anappleisnotatomato"

def letter():
    letter_dict = dict()
    current_most_letter = string[0]
    for letter in string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
        if letter_dict[letter] > letter_dict[current_most_letter]:
            current_most_letter = letter
    return current_most_letter

print(letter())