# This file contains the code for the manipulation of the 
# author_reputation algorithm. The main function is getAuthorReputation,
# which takes the array of versions as input, computes the author
# reputation for each version in the array, and stores them in an array.
# The explanation of other functions can be found on top of the functions.
#
# Cagan Bakirci, November 2019


from author_reputation.article import Article
from author_reputation.version import Version
from author_reputation.author import Author
from author_reputation.edit import Edit

import math
from sys import path
from os.path import dirname as dir

repArray = []
test_article = []
test_versions = []



#################################################################
#
# Create Reputation Array
#
# The function initilizes the repArray
# 
def createRepArray(myArray = []):
    for i in range(len(myArray)):
        repArray.append(Author(i, 0))



#################################################################
#
# get Author Reputation
#
# The function takes an array of versions as input, computes
# the author reputation for each version in the array, and
# stores them in an array.
# 
def getAuthorReputation(arr = [[]]):
    path.append(dir(path[0]))

    max_judgement_dist = 2
    scaling_constant = 1
    scaling_function = lambda x: math.log(1.1 + x)

    test_article = Article(max_judgement_dist, scaling_constant, scaling_function)


    for version_iter in range(len(arr)):
        test_versions.append(Version(arr[version_iter], test_strings[version_iter]))
    
    for x in range(len(arr) - 2):
        for version_iter, version in enumerate(test_versions):
            test_article.add_new_version(version)



#################################################################
#
# get Author and Reputation
#
# The function returns the author and the reputation value for
# the ith version of the article.
# 
def getAuthorAndRep(i):
    return (repArray[i])



#################################################################
#
# get Final Author and Reputation
#
# The function returns the author and the reputation value for
# the final version of the article.
# 
def getFinalAuthorAndRep():
    return(repArray[len(repArray) - 1])



#################################################################
#
# get Reputation Value
#
# The function returns the reputation value for the author
# of the ith version of the article as a float value.
# 
def getRepVal(i):
    return(repArray[i].reputation)



#################################################################
#
# get Final Reputation Value
#
# The function returns the reputation value for the author
# of the final version of the article as a float value.
# 
def getFinalRepVal():
    return (repArray[len(repArray) - 1].reputation)



#The Main Function with some test cases.
if __name__ == '__main__':
    test_strings = []
    #Some cases for testing
    test_strings.append("the quick brown fox jumps over the lazy dog")
    test_strings.append("foo the quick brown fox jumps over the lazy dog bar")
    test_strings.append("the quick brown fox jumps over the lazy dog")
    test_strings.append("the lazy fox jumps over the quick brown dog")
    test_strings.append("the lazy fox jumps over the quick brown dog and also other stuff")

    #Creare the Array
    createRepArray(test_strings)
    #call getAuthorReputation to compute the resulting reputation array
    getAuthorReputation(repArray)

    # TEST
    print("---Printing repArray (final)---")
    print(*repArray)

    print("Author 3")
    print(getAuthorAndRep(3))
    print(getRepVal(3))

    print("---Printing repArray (Final Author)---")
    print(getFinalAuthorAndRep())
    print(getFinalRepVal())

