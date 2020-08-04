import random as r
import datetime
import os

word_file = "words.txt"
word_list = []
password = []

def test_generate_password():
    with open(word_file, 'r') as f:
        for line in f:
            word_list.append(line.strip().lower())

    for _ in range(3):
        password = password.append(word_list[r.randrange(len(word_list))])

        return password


print(test_generate_password())



