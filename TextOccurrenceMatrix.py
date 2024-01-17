from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
  
ps = PorterStemmer()

wordDic = {}
wordList = []
cleanWordList = []

for i in range(5): # Create a dictionary from all the words in 5 Texts
    filename = "text" + str(i) + ".txt"
    text = open(filename,"r")
    text = text.read()
    words = text.split()
    
    for word in words:
        if word not in wordList:
            wordList.append(word)

for word in wordList: # Steam the wordList into cleanWordList
    cleanWordList.append(ps.stem(word))
        
for i in range(5): # Use the dictionary to count how many of each word is in all 5 Texts
    filename = "text" + str(i) + ".txt"
    text = open(filename,"r")
    text = text.read()
    words = text.split()

    for word in cleanWordList:
        num = text.count(word)
        wordDic.update({word: str(num)})

    print("Text Number "+str(i+1)+":")
    print("----------------")
    print(wordDic)
    print("----------------")




