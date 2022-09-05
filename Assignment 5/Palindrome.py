word = input("Enter the word: ")
word = word.lower()
word = word.replace(" ", "")
letters = list(word)
letters = letters[::-1]
wordReverse = ""
for letter in letters:
    wordReverse = wordReverse + letter
if word == wordReverse:
    print("The word is palindrome.")
else:
    print("The word isn't palindrome")
