word = input("Enter the word: ")
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
for character in word:
    for item in vowels:
        if character == item:
            word = word.replace(character, "?")

print(word)
