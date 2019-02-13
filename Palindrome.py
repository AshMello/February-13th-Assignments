word = (input("pick a word! "))
reversed_word = ""
for letters in range(len(word)-1,-1, -1):
    reversed_word += word[letters]

if word.lower() == reversed_word.lower():
    print("Your word is a Palindrome")
else:
    print("Your word is not a Palindrome")

    