sentence = "the quick brown fox jumps over the lazy dog"
sentence = sentence.split()
word_freq = {word: sentence.count(word) for word in sentence}
print(word_freq)


