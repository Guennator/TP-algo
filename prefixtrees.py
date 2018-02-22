__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixTrees.py 2018-02-14'

"""
Prefix Trees homework
2018
@author: corentin.le-guennec
"""


from algopy import tree


################################################################################
## MEASURES

def __countwords(T,nbword):
    for child in T.children:
        if child.key[1]:
            nbword += 1
        nbword = __countwords(child,nbword)
    return nbword

def countwords(T):
    word = __countwords(T,0)
    return word

def longestwordlength(T):
    """ longest word length

    :param T: The prefix tree
    :rtype: int
    :Example:
    >>> longestwordlength(Tree1)
    6
    """
    h = -1
    for child in T.children:
        h = max(h,longestwordlength(child))
    return h + 1




def __averagelength(T, l, length):
    """ average word length

    :param T: The prefix tree
    :rtype: float
    :Example:
    >>> averagelength(Tree1)
    4.636363636363637
    """
    if T.key[1]:
        l += length
    for C in T.children:
        l = __averagelength(C,l,length+1)
    return l

def averagelength(T):
    res = __averagelength(T,0,0)
    words = countwords(T)
    return res/words



###############################################################################
## Researches

def __searchword(T,word,i = 0):
    res = True
    while res:
        res = False
        for j in range(T.nbchildren):
            if i == len(word):
                if T.children[j - 1].key[1] == True:
                    return True
                else:
                    return False
            if T.children[j].key[0] == word[i]:
                res = True
                break
        if T.nbchildren != 0 :
            T = T.children[j]
            i += 1
        else:
            res = False
    return i == len(word)


def searchword(T, word):
    """ search for a word in dictionary

    :param T: The prefix tree
    :param word: The word to search for
    :rtype: bool
    :examples:
    >>> searchword(Tree1, "fabulous")
    False
    >>> searchword(Tree1, "Famous")
    True
    """
    tofind = word.lower()
    return __searchword(T,tofind)

###############################################################################
## Lists
def __wordlist(T,l,current = ""):
    for child in T.children:
        if child.key[1]:
            l.append(current + child.key[0])
        __wordlist(child,l,current + child.key[0])
    return l

def wordlist(T):
    """ generate the word list

    :param T: The prefix tree
    :rtype: list
    :example:
    >>> print(wordlist(Tree1))
    ['case', 'cast', 'castle', 'circle', 'city', 'come', 'could', 'fame', 'famous', 'fan', 'fancy']
    """
    l = []
    return __wordlist(T,l)


def longestwords(T):
    """ search for the longest words in dictionary

    :param T: The prefix tree
    :rtype: list
    :examples: # order in result does not matter
    >>> longestwords(Tree1)
    ['castle', 'circle', 'famous']
    """
    res = []
    l = wordlist(T)
    longest = longestwordlength(T)
    for word in l:
        if len(word) == longest:
            res.append(word)
    return res

def completion(T, prefix):
    """ generate the list of words with a common prefix

    :param T: The prefix tree
    :param pref: the prefix
    :rtype: list
    :examples: # result elements can have different case...
    >>> completion(Tree1, "Fan")
    ['Fan', 'Fancy']
    >>> completion(Tree1, "CI")
    ['Circle', 'City']
    >>> completion(Tree1, "what")
    []
    """
    pref = prefix.lower()
    res = []
    l = wordlist(T)
    for word in l:
        if len(pref) <= len(word):
            match = True
        else:
            match = False
        i = 0
        while i < len(pref) and match:
            if pref[i] != word[i]:
                match = False
            i += 1
        if match:
            res.append(word)
    return res

def treetofile(T, filename):
    """ save the dictionary in a file

    :param T: The prefix tree
    :param filename: the file name
    :example:
    >>> treeToFile(Tree1, "test.txt")
    # give the same file as "textFiles/wordList1.txt" but in alphabetic order
    """
    l = wordlist(T)
    f = open(filename,"w")
    for word in l:
        f.write(word + "\n")
    f.close()


###############################################################################
## Build Tree
def __found_to_add(T, word,i = 0):
    """
    find where a new word should be added ans at what char of the word
    """
    found = False
    j = 0
    while i < len(word) and not(found):
        if j >= T.nbchildren:
            found = True
        else:
            if T.children[j].key[0] == word[i]:
                T = T.children[j]
                j = 0
                i += 1
            else:
                j += 1
    if i == len(word):
        return (T,True,0)
    else:
        return(T,False,i)

def __create_subtree(word,i):
    if i == len(word) - 1:
        T = tree.Tree((word[i],True),[])
    else:
        T = tree.Tree((word[i],False),[])
    if i < len(word) - 1:
        T.children.append(__create_subtree(word,i+1))
    return T

def __addword(node,sub_tree):
    node.children.append(sub_tree)
    ordered = False
    i = node.nbchildren - 1
    while not(ordered):
        if i > 0:
            if node.children[i].key[0] < node.children[i-1].key[0]:
                temp = node.children[i]
                node.children[i] = node.children[i-1]
                node.children[i-1] = temp
            else:
                ordered = True
        else:
            ordered = True
        i -= 1

def addword(T, word):
    """ add a word in dictionary

    :param T: The prefix tree
    :param word: The word to add
    """
    _word = word.lower()
    node,status,indice =  __found_to_add(T,_word)
    if status:
        node.key =(node.key[0], True)
        return True
    else:
        sub_tree = __create_subtree(word,indice)
        __addword(node,sub_tree)
    return T


def treefromfile(filename):
    """ build the prefix tree from a file of words

    :param filename: The file name
    :rtype: Tree
    """
    T = tree.Tree('',[])
    with open(filename,"r") as f:
        for line in f:
            addword(T,line.strip())
    return T
