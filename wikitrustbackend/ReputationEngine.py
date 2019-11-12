# -*- coding: utf-8 -*-
import math

"""
Created on Thu Nov  7 19:22:39 2019

@author: cagan
"""
tArray = []

#################################################################
#
# Parse Array.
#
# The function takes a string version of the edit list read from
# the diff.txt file. The function parses the string and creates
# an array that is used by the other functions. The only argument
# to the function is a string. The functions return an array.
#
def parseArray(read):
    x = read.split(", (")
    myArray = []
    myList = []
    for row in x:
        i = 0
        temp = ""
        while i < len(row):
            # for i in row:
            if isInt(row[i]):
                temp += row[i]
                if isNotInt(row[i + 1]):
                    myList.append(int(temp))
                    i += 1
                else:  # int is > 10
                    # stillInt = isInt(row[i]
                    while isInt(row[i + 1]) > 0:
                        i += 1
                        temp += row[i]
                    myList.append(int(temp))
                    i += 1
            else:
                i += 1
            if len(myList) == 4:
                myTuple = (myList[0], myList[1], myList[2], myList[3])
                myArray.append(myTuple)
                myList = []

            temp = ""
    return myArray


#################################################################
#
# Assign Trust.
#
# The function takes the array version of the edit list returned
# from the parseArray functio. The function computes the trust
# values of each function as well as the overall trust value of
# the text. The function return the overall trust value as an
# integer. The function also modifies the values in tArray[].
#
def assignTrust(array=[[]]):  # Assign a trust value to the text

    if len(array) == 1:
        if array[0][0] == 0 and array[0][1] == 0 and array[0][2] == 0:
            return 100

    currentTrust = 100
    t = 0
    # tt = 0
    for row in array:
        if row[0] == 0:
            t += (0.0001) * row[3]
            tArray.append((0.0001) * row[3])
        elif row[0] == 1:  # insert
            if row[3] < 2:
                t += (0.3) * row[3]
                tArray.append((0.3) * row[3])
            else:
                t += math.log(2, row[3])
                tArray.append(math.log(2, row[3]))

        elif row[0] == 2:
            tArray.append(0)
        else:
            print("INVALID ENTRY")

        # tt += 5 * row[3]
    currentTrust -= t

    return currentTrust


#################################################################
#
# Check Value.
#
# The function is a simple test to see whether the overall trust
# value and the total of individual trust values are matching.
# The function should write OK if values match.
#
def checkVal(val, myArr=[]):  # Test to see if values match
    check = 0
    for j in range(0, len(myArr)):
        check += myArr[j]
    if (100 - check) == val:
        print("OK")
    else:
        print("Something went wrong... value is: " + str(100 - check))


#################################################################
#
# Is Integer and Is Not Integer.
#
# Helper functions used by the parseArray function. The functions
# determine whether a value in a string is an integer or not.
# Both functions return a boolean value as 0 or 1.
#
def isInt(i):
    flag = False
    if i != "[" and i != "," and i != " " and i != ")" and i != "(" and i != "]":
        flag = True
    return flag


def isNotInt(i):
    flag = False
    if i == "[" or i == "," or i == " " or i == ")" or i == "(" or i == "]":
        flag = True
    return flag


#################################################################
#
# Main
#
if __name__ == "__main__":
    f = open("diff1.txt")  # open file to read the edit list
    read = f.readline()  # read the edit list from the file
    f.close()  # close the file
    arr = parseArray(read)  # Convert the string values into an array
    val = assignTrust(arr)  # Compute the trust value
    checkVal(val, tArray)  # Check is the values are matching
    k = open("trustReputation.txt", "w")  # open a file to write the trust value
    k.write(str(val))  # write the trust value
    k.close()  # close the file

