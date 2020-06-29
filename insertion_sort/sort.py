from timeit import default_timer as timer

def get_words():
  fname = "../dataset/words_10000.txt"

  wordlist = []

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())

  return wordlist

# O(n^2) - Best case O(n)
def insertion_sort(wordlist):
  for i in range(1, len(wordlist)):
    key = wordlist[i]
    j = i - 1

    while (j >= 0) and (wordlist[j] > key):
      wordlist[j+1] = wordlist[j]
      j = j - 1

    wordlist[j + 1] = key

wordlist = get_words()
wordlist2 = get_words()

print(wordlist[:10], wordlist[-10:])

tsort = timer()
insertion_sort(wordlist)
tsort = timer() - tsort

tsort2 = timer()
wordlist2.sort()
tsort2 = timer() - tsort2

print(wordlist[:10], wordlist[-10:])
print(wordlist2[:10], wordlist2[-10:])

print(str(tsort), str(tsort2))
