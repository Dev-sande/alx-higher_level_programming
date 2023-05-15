#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if (ln == 0):
        new_tuple = (ln, None)
    else:
        new_tuple = (ln, sentence[0])
    return (new_tuple)

