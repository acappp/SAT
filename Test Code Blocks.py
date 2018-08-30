def ratesort(Movies):
    sortedList = []

    if len(Movies) < 2:
        return Movies

    listLength = len(Movies)
    index = 0
    list1 = []
    list2 = []

    #middle = int(len(listToSort) / 2)

    while index < listLength:
        if (index + 1 <= int((listLength) / 2)):
            list1.append(Movies[index])
        else:
            list2.append(Movies[index])
        index += 1

    returnedList1 = ratesort(list1)
    returnedList2 = ratesort(list2)



    for i in range(0, len(list1) + len(list2)):

        if len(returnedList1) < 1:

            for i in returnedList2:
                sortedList.append(i)
            break

        if len(returnedList2) < 1:
            for i in returnedList1:
                sortedList.append(i)
            break

        if returnedList1[0].rating < returnedList2[0].rating:
            sortedList.append(returnedList1.pop(0))
        elif returnedList2[0].rating < returnedList1[0].rating:
            sortedList.append(returnedList2.pop(0))

        else:
            sortedList.append(returnedList1.pop(0))
            sortedList.append(returnedList2.pop(0))
    Movies = sortedList
    return Movies
