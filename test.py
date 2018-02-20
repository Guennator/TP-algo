from algopy import tree
import prefixtreesexample
import prefixtrees

T = prefixtreesexample.Tree1
#print(prefixtrees.countwords(T))
#print(prefixtrees.longestwordlength(T))
#print(prefixtrees.averagelength(T))
#print()
#print("test fabulous " + str(prefixtrees.searchword(T,"fabulous")))
#print("test Famous " + str(prefixtrees.searchword(T,"Famous")))
#print("test fabulous " + str(prefixtrees.searchword(T,"fabulous")))
#print("test Famous " + str(prefixtrees.searchword(T,"Famous")))
#print()
#print(prefixtrees.wordlist(T))
#print(prefixtrees.longestwords(T))
#print()
#print("fan")
#print(prefixtrees.completion(T,"Fan"))
#print("CI")
#print(prefixtrees.completion(T,"CI"))
#print("what")
#print(prefixtrees.completion(T,"what"))
prefixtrees.treetofile(T,"test.txt")

prefixtrees.addword(T,"cities")
prefixtrees.addword(T,"citation")
prefixtrees.addword(T,"citeration")
#print(prefixtrees.wordlist(T))
prefixtrees.treetofile(T,"test.txt")
B = prefixtrees.treefromfile("textFiles/wordList1.txt")
prefixtrees.treetofile(B , "test.txt")
C = prefixtrees.treefromfile("textFiles/wordList2.txt")
prefixtrees.treetofile(C , "test2.txt")
