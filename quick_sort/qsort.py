import csort
from timeit import default_timer as timer 

#fname = "../dataset/words_320139.txt"
fname = "../dataset/words_10000.txt"

def get_words():  
  wordlist = []

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())
  
  return wordlist

def get_wordsC():
  wordlist = csort.VectorString()

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())
  
  return wordlist


# O(n log(n))
def quick_sort(wordlist, low, up):
  if low < up:
    pivot = partition(wordlist, low, up)
    quick_sort(wordlist, low, pivot-1)
    quick_sort(wordlist, pivot, up)

def partition(worlist, low, up):
  center = (up - low) >> 1 # (low + up) / 2
  pivot = wordlist[low + center]
  i = low
  j = up

  while True:
    while wordlist[i] < pivot:
      i = i + 1
    
    while wordlist[j] > pivot:
      j = j - 1
    
    if i >= j:
      break
    
    aux = wordlist[i]
    wordlist[i] = wordlist[j]
    worlist[j] = aux
    i = i + 1
    j = j - 1
  
  aux = wordlist[i]
  wordlist[i] = wordlist[up]
  worlist[up] = aux

  return i

wordlist = get_words()
wordlist2 = get_words()
wordlist3 = get_wordsC()

tsort = timer()
quick_sort(wordlist, 0, len(wordlist) - 1)
tsort = timer() - tsort

tsort2 = timer()
wordlist2.sort()
tsort2 = timer() - tsort2

tsort3 = timer()
wordlist3.quicksort()
tsort3 = timer() - tsort3

print(wordlist[:10], wordlist[-10:])
print(wordlist2[:10], wordlist2[-10:])
print(wordlist3[:10], wordlist3[-10:])
print("Python: ", tsort, ", Default: ", tsort2, ", C++:", tsort3)
