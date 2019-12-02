from text_trust.version import Version
from text_trust.block import Block
from text_trust.edit import Edit
from text_trust.word import Word

from chdiff import test_tichy, test_greedy, print_edit_diff

versionArray = []
authorRepArr = []
trustArray = [[]]
#sentenceArray = []
mm = 0
ii = 0
dd = 0 

def getEditCountArray():
    return [mm, ii, dd]

#################################################################
#
# get Reputation Array.
#
# The function takes the array of versions as strings and 
# computes the trust values of each word in all the versions.
# 
def getRepArray(myArray=[[]], initial_trust=1, authorRepArr=[]):
    repArray = [[] for _ in range(len(myArray) - 1)] #Create an array for each version
    text_list = myArray[0].split()


    trust_inheritance_const = 0.5
    revision_const = 0.1
    edge_effect_const = 2

    constants = (trust_inheritance_const, revision_const, edge_effect_const)

    ver = Version.create_initial_version(text_list, initial_trust, constants)
    #print(repArray)
    #print("Version 1:\n")
    #print("Initial Trust: " + str(initial_trust) + "\n")
    run = True
    mov = 0
    ins = 0
    dele = 0
    for string_iter in range(len(myArray)-1):
        #print("Version %d:\n" % (string_iter + 2))
        #print("Author Reputation: %d\n" % (authorRepArr[string_iter]))
        #if(string_iter == 0)


        diff_list = test_tichy(myArray[string_iter], myArray[string_iter + 1])
        # print("diff_list")
        # print(diff_list)
        # print("")

        edit_list = [Edit.edit_tuple_constructor(edit) for edit in diff_list]
        # print("edit_list")
        # print(edit_list)
        # print("")

        if run:
            run = False
            for e in edit_list:
                if e.edit_type == 0:
                    mov += 1
                elif e.edit_type == 1:
                    ins += 1
                else:
                    dele += 1


        text_list = myArray[string_iter+1].split()
        # print("text_list")
        # print(text_list)
        # print("")

        ver = Version.create_next_version(ver, text_list, edit_list, authorRepArr[string_iter])
        # print("ver")
        # print(ver)
        # print("")
        #myArray[string_iter].join(ver.word_list[0].trust)
        #repArray[string_iter] + (ver.word_list[0].trust)
        
        #repArray[string_iter].append(ver.word_list[0].trust)
        for i in range(len(ver.word_list)):
            repArray[string_iter].append(round(ver.word_list[i].trust, 2))
        #print(repArray)

       # print("".join([str(word) for word in ver.word_list]) + "\n")
    return [repArray, mov, ins, dele]  



#################################################################
#
# get Word Array.
#
# The function get the word array in version i
# 
def getWordArray(i):
    txtArr = []

    #for i in versionArray
    txtArr = versionArray[i].split()

    return txtArr



#################################################################
#
# get Final Word Array.
#
# The function get the word array of the final version 
# 
def getFinalWordArray():
    txtArray = []

    #for i in versionArray
    txtArray = versionArray[len(versionArray) - 1].split()

    return txtArray



#################################################################
#
# get Overall Trust.
#
# The function returns the overall trust value of ith version
# 
def getOverallTrust(i, trustArray):
    if (i > len(trustArray[i - 1])):
        exit() #HANDLE THIS!

    num = 0
    if (i < 0):
        num = 1
    else:
        for j in range(len(trustArray[i - 1])):
            num += trustArray[i - 1][j]

        if len(trustArray[i-1]) > 0:
            num = round((num / len(trustArray[i - 1])), 2)
        else:
            num = round(num, 2)
        
    return num



#################################################################
#
# get Final Overall.
#
# The function returns the overall trust value of the final version
# 
def getFinalTrust(trustArray):
    return getOverallTrust(len(trustArray)-1, trustArray)



#################################################################
#
# combine Trust with Text
#
# The function returns an array that consist of each word in a 
# revision and the corresponding trust values of that word in 
# ith revision. 
# 
def combineTrustWithText(i, myArr = [[]]):
    arr = [str, 0]
    #myArray = [()]
    myArray = []
    if (i > len(trustArray[i - 1])):
        print("HANDLE ME!")
    if (trustArray.count == 0):
        print("HANDLE ME!")
    
    #for word in myArr[i]:
    temp = myArr[i].split()
    for j in range(len(trustArray[i - 1])):
        arr.append("".join(temp[j - 1] + " " + str(trustArray[i - 1][j])))
        #myArray.append((temp[j], trustArray[i - 1][j]))
        #myArray.append("(%s, %.2f)" % (temp[j], trustArray[i - 1][j]))
        # txt = temp[j]
        # val = round((trustArray[i - 1][j]), 2)
        # myArray.append((txt, val))
        myArray.append((temp[j], round((trustArray[i - 1][j]), 2)))
        
    return myArray 



#################################################################
#
# combine Trust with Sentences
#
# The function returns an array that consist of each sentence in  
# a revision and the corresponding trust values of that sentence 
# in the revision. 
# 
#def combineTrustWithSentences(wordArray=[[]], trustArray=[[]]):






#################################################################
#
# get Trust Values.
#
# The function returns the trust values of ith version
# 
def getTrustValues(i):
    if (i > len(trustArray[i - 1])):
        exit() #HANDLE THIS!
    
    #if(i < 1)
    #    returnVal = 

    return (trustArray[i - 1])

#################################################################
#
# get Final Trust Values.
#
# The function returns the trust values of the final version
# 
def getFinalValues():
    return getTrustValues(len(trustArray))



if __name__ == '__main__':
    """
    An example of using text_trust.py. The test strings are the different
    texts of different versions. The test_trusts list is the different
    author_reputations of each version.
    """
    initial_trust = 1

    test_strings = []
    # test_strings.append("'WikiTrust' is a [[software product]] that assesses the credibility of content and author reputation of [[wiki]] articles using an automated [[algorithm]]. WikiTrust is a [[Plug-in (computing)|plug-in]] for servers using the [[MediaWiki]] platform, such as [[Wikipedia]]. When installed on a [[MediaWiki]] website it is designed to enable users of that website to obtain information about the author, origin, and reliability of that website's wiki text.<ref name=mainucsc/> Content that is stable, based on an analysis of article history, should be displayed in normal black-on-white type, and content that is not [[wikt:stable#Adjective|stable]] is highlighted in varying shades of yellow or orange.")
    # test_strings.append("When the UCSC server was active, WikiTrust assessed the credibility of content and author reputation of [[wiki]] articles using an automated [[algorithm]]. WikiTrust provides a [[Plug-in (computing)|plug-in]] for servers using the [[MediaWiki]] platform, such as [[Wikipedia]]. When installed on a [[MediaWiki]] website it was designed to enable users of that website to obtain information about the author, origin, and reliability of that website's wiki text.<ref name=mainucsc/> Content that is stable, based on an analysis of article history, should be displayed in normal black-on-white type, and content that is not [[wikt:stable#Adjective|stable]] is highlighted in varying shades of yellow or orange.  It was formerly available for several language versions of Wikipedia.")
    # test_trusts = [10, 7]

    test_strings.append("the quick brown fox jumps over the lazy dog.")
    test_strings.append("foo the quick brown fox jumps over the lazy dog bar.")
    test_strings.append("the quick brown fox jumps over the lazy dog.")
    test_strings.append("the lazy fox jumps over the quick brown dog.")
    test_strings.append("the lazy fox jumps over the quick brown dog and also other stuff.")
    test_trusts = [10, 7, 10, 20]

    authorRepArr = test_trusts

    versionArray = test_strings

    trust_inheritance_const = 0.5
    revision_const = 0.1
    edge_effect_const = 2

    constants = (trust_inheritance_const, revision_const, edge_effect_const)

    sentenceArray = []

    trustArray = getRepArray(test_strings) 
    print(trustArray)
    print("")
    print("")
    print("TESTING getOverallTrust & getFinalTrust")
    #print("Version 1 trust: ", getOverallTrust(0))
    print("Version 1 trust: ", getOverallTrust(1))
    print("Version 2 trust: ", getOverallTrust(2))
    print("Version 3 trust: ", getOverallTrust(3))
    print("Version 4 trust: ", getOverallTrust(4))
    print ("Final Trust: ", getFinalTrust())
    print("")
    print("")
    print("TESTING getTrustValues & getFinalTrustValues")
    #print("Version 0: ", getTrustValues(0))
    print("Version 1: ", getTrustValues(1))
    print("Version 2: ", getTrustValues(2))
    print("Version 3: ", getTrustValues(3))
    print("Version 4: ", getTrustValues(4))
    print("Final Values: ", getFinalValues())

    print("TESTING combineTrustWithText")
    print("Combined 1: ", combineTrustWithText(1, test_strings))

    print("TESTING getWordArray & getFinalWorldArray")
    sentenceArray = getWordArray(2)
    print (sentenceArray)
    finalArr = getFinalWordArray()
    print (finalArr)