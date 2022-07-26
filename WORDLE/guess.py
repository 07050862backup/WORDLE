"""author --- 07050862"""
WORDLIST_FILENAME = "fiveletter.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def Compare_letter_locate(wordlist,index,letter): #篩選出位置一樣的單字
    correct_wordlist=[]
    for i in range(len(wordlist)):
        for j in range(5):
            if j == index and wordlist[i][j] == letter:
                correct_wordlist.append((wordlist[i]))
    return correct_wordlist
def get_ord(word):
    ordlist = []
    for e in word:
        o = ord(e)
        ordlist.append(o)
    return ordlist
def get_chr(word):
    charlist = []
    for e in word:
        c = chr(e)
        charlist.append(c)
    return charlist
def splitwordlist_to_abc(wordlist):
    chrlist = []
    for word in wordlist:
        ordlist = get_ord(word)
        # print(ordlist)
        chrlist.append(get_chr(ordlist))
        # print(chrlist)
        # print(''.join(chr_))
    return chrlist
def list_to_dict(wordlist):
    dictlist = []
    for i in range(len(wordlist)):
        dictlist.append(set(splitwordlist_to_abc(wordlist)[i]))
    return dictlist # [{'g', 's', 'r', 'a'}, {'h', 's', 'e', 'p'},...]

""" 匯入字母 """
fiveword = loadWords()


dictlist = list_to_dict(fiveword)

print("前5筆資料:\n{}\n{}".format(fiveword[0:5],dictlist[0:5]))
# print(fiveword) #['aback', 'abaft',....]
# print(dictlist)  #[{'b', 'c', 'k', 'a'}, {'b', 'f', 't', 'a'},....]

print("篩選正確的字母:\n")


wordlist2 = Compare_letter_locate(fiveword,0,'a')# 篩選第1個字母是o的
#wordlist2 = Compare_letter_locate(wordlist2,0,'a')# 篩選第1個字母是o的

dictlist2 = list_to_dict(wordlist2)
# print(wordlist2)
# print(dictlist2)
dict_from_list = {wordlist2[i]: dictlist2[i] for i in range(len(wordlist2))}
print("dict_from_list:\n{}".format(dict_from_list))
notinword = {'o','r','l','d','i','n','g'}
inword = {'w','a'}

anslist = []
for key, value in dict_from_list.items():
    #print(key, 'corresponds to', value)
    if (len(value & notinword) ==0) and (len(value & inword) >= len(inword)) :
        anslist.append(key)
print("符合的單字有:\n")
print(anslist)

