from timeit import default_timer as timer

def get_words():
  fname = "../dataset/words_10000.txt"

  wordlist = []

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())

  return wordlist

# O(n^2)
def selection_sort(wordlist):
  length = len(wordlist)

  for i in range(length):
    for j in range(i+1, length):
      if wordlist[i] > wordlist[j]:
        aux = wordlist[i]
        wordlist[i] = wordlist[j]
        wordlist[j] = aux

if __name__ == "__main__":
  wordlist = get_words()
  wordlist2 = get_words()

  print(wordlist[:10], wordlist[-10:])

  tsort = timer()
  selection_sort(wordlist)
  tsort = timer() - tsort

  tsort2 = timer()
  wordlist2.sort()
  tsort2 = timer() - tsort2

  print(wordlist[:10], wordlist[-10:])
  print(wordlist2[:10], wordlist2[-10:])
  print(tsort, tsort2)

