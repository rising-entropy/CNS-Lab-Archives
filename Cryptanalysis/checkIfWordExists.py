import enchant

d = enchant.Dict("en_US")
print("Enter the word to check: ", end='')
word = input()
print()
if d.check(word):
    print(word, "is a valid word!")
else:
    print(word, "is an invalid word!")