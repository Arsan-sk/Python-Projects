print("Welcome To My GK Quiz!")

playing = input("Do You want to PLAY? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does Ai stand's For? ")

if answer.lower() == "artificial intelligence" :
    print("correct!")
    score += 1

else :
    print("Incorrect!")


answer = input("Who is the author of 'To Kill a Mockingbird'? ")

if answer.lower() == "harper lee" :
    print("Correct!")
    score += 1

else :
    print("Incorrect!")


answer = input("What is the capital city of France? ")

if answer.lower() == "paris" :
    print("Correct!")
    score += 1

else :
    print("Incorrect!")


answer = input("What is the largest island in the world? ")

if answer.lower() == "greenland" :
    print("Correct!")
    score += 1

else :
    print("Incorrect!")

print("You Got " + str(score) + " Questions Correctly!")
print("You Got " + str((score/4)*100) + "% Percentage")
