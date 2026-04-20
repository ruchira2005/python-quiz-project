print(" Welcome to the Quiz Game!")

name = input("Enter your name: ")
print("Hello", name, "! Let's start the quiz.\n")

score = 0
ans1 = input("1. what is 10+55: ")
if ans1.lower() == "65":
    print("Correct")
    score += 1
else:
    print("Wrong")
ans2 = input("2. 5 + 3 = ")
if ans2 == "8":
    print("Correct")
    score += 1
else:
    print("Wrong")
ans3 = input("3. 8*10-5 =  ")
if ans3.lower() == "75":
    print("Correct")
    score += 1
else:
    print("Wrong")
print("your score is:",score)

if score == 3:
    print("Excellent, You got all answers correct")
elif score == 2:
    print("Good job, Almost perfect")
elif score == 1:
    print("Not bad, keep practicing")
else:
    print("Better luck next time")