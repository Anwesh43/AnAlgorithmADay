def get2ndMostElem(words):
    wordDict = {}
    mostRepeated = 0
    secMostRepeated = 0
    secCurrWord = None
    currWord = None
    for word in words:
        if word in wordDict:
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
        count = wordDict[word]
        if count > mostRepeated:
            mostRepeated = count
            if not(currWord == word):
                secCurrWord = currWord
                currWord = word
        elif count >= secMostRepeated:
            secMostRepeated = count
            secCurrWord = word
    print(mostRepeated)
    print(secMostRepeated)
    return secCurrWord
def main():
    words = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
    print(get2ndMostElem(words))
if __name__ == "__main__":
    main()
