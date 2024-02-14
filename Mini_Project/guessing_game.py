import random #To generate random thing

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the number from(1 - 100) or Quit : ")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct Guess...!!")
        break
    elif(userChoice < target):
        print("You're guess too small. Take a bigger number...")
    else:
        print("You're guess too large. Take a smaller number...")
    
print("-----GAME OVER-----")