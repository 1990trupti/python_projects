print("Welcome to my Computer Quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's start the game. ")
score = 0

question = input("GPU stands for?")
if question.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("FIFO stands for?")
if question.lower() == "first in first out":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("FTP stands for?")
if question.lower() == "file transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("CPU stands for?")
if question.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("LISP is?")
if question.lower() == "list programming language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("you got " + str(score) + " correct Answers")
print("you got " + str((score/5)*100) + " %")

