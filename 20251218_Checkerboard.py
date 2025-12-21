** start of main.py **

def create_board(dimensions):
    pattern = [["X", "O"],["O", "X"]]

    length = dimensions[1]
    row = dimensions[0]

    finalArray = []
    rowCount = 1

    for each in range(1,row + 1):
        perRow = []
        # Divided by % 2 becomes either 0 for even or 1 for odd
        if each % 2 == 1:
            rowPat = pattern[0]
        else:
            rowPat = pattern[1]
        
        for eachChar in range(length):
            if eachChar % 2 == 0:
                perRow.append(rowPat[0])
            else:
                perRow.append(rowPat[1])
        
        finalArray.append(perRow)

    print(finalArray)
    return finalArray



create_board([3, 3])
print("------------")
create_board([6, 1])
print("------------")
create_board([2, 10])
print("------------")
create_board([5, 4]) 

** end of main.py **

