import secrets

print("Welcome to our program that will allow you to generate a quick password! In order to do so" +
"you will need to provide us with 4 different words.")
print("")

givenWords = input("Please provide 4 different words, separate them with a space")
print("")

givenWordList = givenWords.split()
print("Here is your list of words.", givenWordList)
print("")

print("We will now turn those 4 words into a password.")
print("")
password = secrets.choice(givenWordList) + secrets.choice(givenWordList) + secrets.choice(givenWordList) + secrets.choice(givenWordList)

print("Your new password is:", password)
