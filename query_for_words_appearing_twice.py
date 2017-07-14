## find number of words that appear exactly twice in an array of words
def queryForTwiceWords(words):
    words = sorted(words)
    k = 0
    if len(words)>0:
        prev_word = words[0]
        c = 0
        for i in range(1,len(words)):
            word = words[i]
            if word == prev_word:
                c = c+1
            elif c == 1:
                k = k+1
                c = 0
            else:
                c = 0
            prev_word = word

    return k
words = ["Om", "Om", "Shankar", "Tripathi", "Tom", "Jerry", "Jerry"]
print queryForTwiceWords(words)
