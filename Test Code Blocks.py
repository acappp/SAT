"""
Merge Sort.py
Author: Stuart Thornhill
Date created: 2/8/2018
Description:
This CLI program will ask for a set of numbers from the user, one number at
a time, once the user presses enter with no value it will print the list
of numbers and run the MergeSort function and reprint the list sorted
"""

#Merge sort function, recursively sorts 2 lists
def MergeSort(listToSort):

    #Check to see if the list is only a single item, if so return the single item list
    if(len(listToSort) < 2):
        return listToSort

    #Setting up initial variable for splitting lists
    listLength = len(listToSort)
    index = 0
    list1 = []
    list2 = []

    #Loop that splits 1 list into 2 lists of roughly equal length
    while index < listLength:
        if(index+1 <= int((listLength)/2)):
            list1.append(listToSort[index])
        else:
            list2.append(listToSort[index])
        index += 1

    #Take our 2 lists, and give one each to a recursive call of MergeSort (this function)
    returnedList1 = MergeSort(list1)
    returnedList2 = MergeSort(list2)

    #Initise the list to return
    sortedList = []

    #This loop will run based on the total length of both lists
    for i in range(0, len(list1)+len(list2)):
        #We check if we are out of value for list1
        if len(returnedList1) < 1:
            #If we are out of values append the rest of list2 and end the loop
            for i in returnedList2:
                sortedList.append(i)
            break
        #Same as above, only for list2, then appending list1
        if len(returnedList2) < 1:
            for i in returnedList1:
                sortedList.append(i)
            break
        #Check which value is smaller and add that next to the sorted list
        if returnedList1[0] < returnedList2[0]:
            sortedList.append(returnedList1.pop(0))
        elif returnedList2[0] < returnedList1[0]:
            sortedList.append(returnedList2.pop(0))
        #Values must be equal, add both to sorted list
        else:
            sortedList.append(returnedList1.pop(0))
            sortedList.append(returnedList2.pop(0))

    return sortedList


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
list = MergeSort(userList)

print("The sorted list is:2")
print(list)