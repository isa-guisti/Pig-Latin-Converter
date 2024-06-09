def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

# store user input
sentence = input()
words = sentence.split()
result = []

for word in words:
    if word:
        first_letter = word[0]

        # first letter is a vowel
        if is_vowel(first_letter):
            result.append(word + "way")
        
        # first letter is a consonant or a series of consonants
        elif is_consonant(first_letter):
            cluster = ''
            rest_of_word = word
            while rest_of_word and is_consonant(rest_of_word[0]):
                cluster += rest_of_word[0]
                rest_of_word = rest_of_word[1:]
            result.append(rest_of_word + cluster + "ay")

final_result = ' '.join(result)
print(final_result)