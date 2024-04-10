Start = input("Are you want to start the game : ")
if Start.lower() != "yes":
    exit()
else:
    print("Let's go to the quiz game")
Score = 0
question1 = input("Which of the following is the correct extension of the Python file? ")
if question1.lower() == ".py":
    print("congratulations Let's move to the next question")
    Score += 1
else:
    print("Let's try another time")
question2 = input("Who developed Python Programming Language? ")
if question2.lower() == "guido van rossum":
    print("congratulations Let's move to the next question")
    Score += 1
else:
    print("Let's try another time")
question3 = input("Which keyword is used for function in Python language? ")
if question3.lower() == "def":
    print("congratulations Let's move to the next question")
    Score += 1
else:
    print("Let's try another time")
question4 = input("Which of the following is the truncation division operator in Python? ")
if question4.lower() == "//":
    print("congratulations Let's move to the next question")
    Score += 1
else:
    print("Let's try another time")
question5 = input("Which of the following is not a core data type in Python programming ")
if question5.lower() == "class":
    print("congratulations")
    Score += 1
else:
    print("Lets try another time")
print(f"Congratulations, Your total score is {Score}")
