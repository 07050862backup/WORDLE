"""author --- 07050862"""
WORDLIST_FILENAME = "words.txt"

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


""" 匯入字母 """
wordlist = loadWords()
fiveword = []
""" 找出只有5個字母的字 """
for i in range(len(wordlist)):
    if len(wordlist[i])==5:
        fiveword.append(wordlist[i])#['grass', 'sheep',...]

f = open('fiveletter.txt', 'a', encoding='utf-8')



for line in fiveword:
    f.write(line+' ')

f.close()