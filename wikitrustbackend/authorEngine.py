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

def createRepArray(myArray = []):
    for i in range(len(myArray)):
        repArray.append(Author(i, 0))


def getAuthorReputation(arr = [[]]):
    # print(path)

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

def getARepVal(i):
    return (repArray[i])

def getFinalAuthor():
    return(repArray[len(repArray) - 1])

def getRepVal(i):
    return(repArray[i].reputation)

def getFinalRepVal():
    return (repArray[len(repArray) - 1].reputation)

if __name__ == '__main__':
    test_strings = []
    test_strings.append("the quick brown fox jumps over the lazy dog")
    test_strings.append("foo the quick brown fox jumps over the lazy dog bar")
    test_strings.append("the quick brown fox jumps over the lazy dog")
    test_strings.append("the lazy fox jumps over the quick brown dog")
    test_strings.append("the lazy fox jumps over the quick brown dog and also other stuff")

    #print("---Printing repArray (before)---")
    #print(repArray)
    createRepArray(test_strings)
    #print("---Printing repArray (after)---")
    #print(*repArray)

    # max_judgement_dist = 2
    # scaling_constant = 1
    # scaling_function = lambda x: math.log(1.1 + x)

    # test_article = Article(max_judgement_dist, scaling_constant, scaling_function)

    #print("///////////////////////////////")
    #dumyArr = getAuthorReputation(repArray)
    getAuthorReputation(repArray)
    # print(*dumyArr)


    print("---Printing repArray (final)---")
    print(*repArray)
    for author in repArray:
        print(str(author))
    print()

    print("Author 3")
    print(getARepVal(3))
    print(getRepVal(3))

    print("---Printing repArray (Final Author)---")
    print(getFinalAuthor())
    print(getFinalRepVal())

    # print("-------------------------")
    # print("-------------------------")
    # print("-------------------------")
    # print("Print test_versions")
    # print(*test_versions)
    # print(" ")
    # print("Print text_article")
    # print(test_article)

    # max_judgement_dist = 2
    # scaling_constant = 1
    # scaling_function = lambda x: math.log(1.1 + x)

    # test_article = Article(max_judgement_dist, scaling_constant, scaling_function)

    # for x in range(3):
    #     for version_iter, version in enumerate(test_versions):
    #         print("Loop %d:\n" % version_iter)

    #         print("Author Status:")
    #         for author in test_authors:
    #             print(str(author))
    #         print()

    #         print("Adding Version...")
    #         print(str(version))
    #         test_article.add_new_version(version)




# Author Status:
# Author ID: 0    Reputation:-1.954446438117569
# Author ID: 1    Reputation:-0.9109152895432457
# Author ID: 2    Reputation:0.8892259506657838
# Author ID: 3    Reputation:0.003016763046310933
# Author ID: 4    Reputation:-0.46862714935921274