#count words in sentences
def countWordOccurrences(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

sentence = "Hi hi hello test test test now"
print(countWordOccurrences(sentence))