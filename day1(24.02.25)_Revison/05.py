def highestScores(scores):
    return max(scores, key=scores.get)

scores={"John": 100, "Jane": 900, "Jack": 90, "Jill": 80}
print(highestScores(scores)) # ["John", "Jane"]