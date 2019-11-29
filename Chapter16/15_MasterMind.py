"""
    16.15 Master Mind
"""
from collections import defaultdict

def getSimilarity(guess, actual):
    # remove hit
    guess = list(guess)
    actual = list(actual)
    hit = 0
    dictGuess = defaultdict(int)
    remaining = []
    for g, a in zip(guess, actual):
        if g == a:
            hit += 1
        else:
            dictGuess[a] += 1
            remaining.append(g)
    pseudoHit = 0
    for r in remaining:
        if dictGuess[r] > 0:
            pseudoHit += 1
            dictGuess[r] -= 1
    return hit, pseudoHit

if __name__ == "__main__":
    print(getSimilarity("RGBY", "GGRR"))