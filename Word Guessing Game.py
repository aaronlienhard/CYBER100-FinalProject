import secrets

print("Welcome to our word guessing game. The way this game works is the computer " + 
      "will give you hints that will lead you to guess the correct word.")
print("")
input("In order to start, press any key on your keyboard and then press 'enter' ")
print("")

listOfWords = ["dog", "cat", "tree", "sky", "chair"]

wordAnswer = secrets.choice(listOfWords)

dogHints = ["This animal can be owned as a pet.", "This pet can fend off intruders if tough enough.", "Sometimes known as 'man's best friend.'"]
catHints = ["This animal can be owned as a pet.", "People argue whether they like this one or another pet more.", "Signiture sound rhymes with 'bow' (take a bow)."]
skyHints = ["It's over you at all times.", "This thing is big and blue.", "'What's up?', 'The ___.''"]
treeHints = ["Will find a lot if you walk outside.", "Can tell their age based on rings.", "They have leaves that can change colors with the season in specific areas."]
chairHints = ["Made from many different materials.", "They are in every classroom.", "You might be sitting in one right now."]

print("Okay, your first hint is...")

if wordAnswer == "dog":
    print(dogHints[0])
    print("")
    
    userAnswer = input("What is your first guess? ")
    print("")
    
    if userAnswer != "dog":
        print("Sorry that was an incorrect guess. Please read your next hint.")
        print("")
        print("Your second hint is...")
        print(dogHints[1])
        print("")
        
        userAnswer = input("What is your second guess? ")
        print("")
        
        if userAnswer != "dog":
            print("Sorry that was an incorrect guess. Please read your final hint.")
            print("")
            print("Your final hint is...")
            print(dogHints[2])
            print("")
            
            userAnswer = input("What is your final guess? ")
            print("")           
        
        if userAnswer != "dog":
            print("Sorry you were unable to guess the correct word. The correct word was 'dog.'")
    else:
        print("Correct, you have guessed the correct word!")
    
    
elif wordAnswer == "cat":
    print(catHints[0])
    print("")
    
    userAnswer = input("What is your first guess? ")
    print("")
    
    if userAnswer != "cat":
        print("Sorry that was an incorrect guess. Please read your next hint.")
        print("")
        print("Your second hint is...")
        print(catHints[1])
        print("")
        
        userAnswer = input("What is your second guess? ")
        print("")  
        
        if userAnswer != "cat":
            print("Sorry that was an incorrect guess. Please read your final hint.")
            print("")
            print("Your final hint is...")
            print(catHints[2])  
            print("")
                    
            userAnswer = input("What is your final guess? ")
            print("")            
        
        if userAnswer != "cat":
            print("Sorry you were unable to guess the correct word. The correct word was 'cat.'")
    else:
        print("Correct, you have guessed the correct word!")
    
elif wordAnswer == "tree":
    print(treeHints[0])
    print("")
    
    userAnswer = input("What is your first guess? ")
    print("")
    
    if userAnswer != "tree":
        print("Sorry that was an incorrect guess. Please read your next hint.")
        print("")
        print("Your second hint is...")
        print(treeHints[1])
        print("")
        
        userAnswer = input("What is your second guess? ")
        print("")  
        
        if userAnswer != "tree":
            print("Sorry that was an incorrect guess. Please read your final hint.")
            print("")
            print("Your final hint is...")
            print(treeHints[2])  
            print("")          
        
            userAnswer = input("What is your final guess? ")
            print("")  
            
        if userAnswer != "tree":
            print("Sorry you were unable to guess the correct word. The correct word was 'tree.'")
    else:
        print("Correct, you have guessed the correct word!")
    
elif wordAnswer == "sky":
    print(skyHints[0])
    print("")
    
    userAnswer = input("What is your first guess? ")
    print("")
    
    if userAnswer != "sky":
        print("Sorry that was an incorrect guess. Please read your next hint.")
        print("")
        print("Your second hint is...")
        print(skyHints[1])
        print("")
        
        userAnswer = input("What is your second guess? ")
        print("")
        
        if userAnswer != "sky":
            print("Sorry that was an incorrect guess. Please read your final hint.")
            print("")
            print("Your final hint is...")
            print(skyHints[2])  
            print("")
            
            userAnswer = input("What is your final guess? ")
            print("")            
        
        if userAnswer != "sky":
            print("Sorry you were unable to guess the correct word. The correct word was 'sky.'")
    else:
        print("Correct, you have guessed the correct word!")
    
elif wordAnswer == "chair":
    print(chairHints[0])
    print("")
    
    userAnswer = input("What is your first guess? ")
    print("")
    
    if userAnswer != "chair":
        print("Sorry that was an incorrect guess. Please read your next hint.")
        print("")
        print("Your second hint is...")
        print(chairHints[1])
        print("")
        
        userAnswer = input("What is your second guess? ")
        print("")  
        
        if userAnswer != "chair":
            print("Sorry that was an incorrect guess. Please read your final hint.")
            print("")
            print("Your final hint is...")
            print(chairHints[2]) 
            print("")
            
            userAnswer = input("What is your final guess? ")
            print("")             
        
        if userAnswer != "chair":
            print("Sorry you were unable to guess the correct word. The correct word was 'chair.'")
    else:
        print("Correct, you have guessed the correct word!")