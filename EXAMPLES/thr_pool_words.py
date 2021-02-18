#!/usr/bin/env python
from multiprocessing.dummy import Pool
import random
import time

NUM_ITEMS = 25000
POOL_SIZE = 64

class RandomWord():  # <3>
    def __init__(self):
        with open('../DATA/words.txt') as words_in:
            self._words = [word.rstrip('\n\r') for word in words_in.readlines()]
        self._num_words = len(self._words)

    def __call__(self):
        return self._words[random.randrange(0, self._num_words)]

def modify_word(word):  # <6>
    return word.upper() + '-' + word.upper()

# <10>
words_to_process = []
random_word = RandomWord()
for i in range(NUM_ITEMS):
    w = random_word()
    words_to_process.append(w)

start_time = time.ctime()

pool = Pool(POOL_SIZE)  #  2 4 8 16 32 64

processed_words = pool.map(modify_word, words_to_process)

end_time = time.ctime()

print(processed_words[:20])

print(start_time)
print(end_time)
