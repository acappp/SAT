
# --------- MAIN PROGRAM ----------
print("Please enter whole number values for the list one at a time.")

userList = []
userInput = "\n"
while(not(userInput == "")):
    userInput = input(":")
    if(not(userInput == "")):
        try:
            userInput = int(userInput)
            userList.append(userInput)
        except ValueError:
            print("Value entered was not a numeric whole number")

print("The list entered was:")
print(userList)


print("The sorted list is:2")
print(list)