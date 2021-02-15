first_letters = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]  # get 1st letter of word

        # if first_letter not in first_letters:  # if letter not a key in dict
        #     first_letters[first_letter] = 0
        # first_letters.setdefault(first_letter, 0)
        first_letters[first_letter] = first_letters.get(first_letter, 0) + 1

        # prev_value = first_letters[first_letter]
        # first_letters[first_letter] = prev_value + 1  # overwrite value

print(first_letters)