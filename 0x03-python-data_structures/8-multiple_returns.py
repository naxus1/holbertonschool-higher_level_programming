#!/usr/bin/python3
def multiple_returns(sentence):
    a = None
    len_sentence = len(sentence)
    if len_sentence > 0:
                a = sentence[0]
    new_tuple = len_sentence, a
    return new_tuple
