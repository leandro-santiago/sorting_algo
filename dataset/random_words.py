import random
import sys

if len(sys.argv) == 1:
  print("python3 random_words.py <number of words>")
  exit()

n_words = int(sys.argv[1])
fname = "words.txt"

wordlist = []

with open(fname, "r") as fd:
  for line in fd:
    wordlist.append(line.strip())

if n_words == 0:
  n_words = len(wordlist)

random_indexes = random.sample(range(0, len(wordlist)), n_words)

outfilename = "words_" + str(n_words) + ".txt"

with open(outfilename, "w") as fd:
  for index in random_indexes:
    fd.write(wordlist[index] + "\n")
