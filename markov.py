import string
import random


def markov(text, length):
    mark = dict()
    i = 0
    while i < len(text) - length:
        prefix = ' '.join(text[i:i + length])
        if prefix not in mark:
            mark[prefix] = [text[i + length]]
        else:
            mark[prefix].append(text[i + length])
        i += 1
    return mark


def chain(mark, length, prefix):
    sentence = []
    i = 0
    start = random.choice(list(mark.keys()))
    sentence.extend(start.split())
    while i < length:
        next = random.choice(mark[start])
        sentence.append(next)
        start = ' '.join(sentence[-prefix:])
        i += 1
    return(' '.join(sentence))
