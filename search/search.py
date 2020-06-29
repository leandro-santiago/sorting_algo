import sys
from timeit import default_timer as timer

def get_words():
  fname = "../dataset/words_320139.txt"
  wordlist = []

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())

  return wordlist

# O(n)
def search(word, wordlist):
  for i in range(len(wordlist)):
    if wordlist[i] == word:
      return i
  
  return -1

# O(log(n))
def bin_search(word, wordlist):
  low = 0 
  up = len(wordlist) - 1

  while low < up:
    mean = (low + up) >> 1 # (low + up)/2

    if wordlist[mean] == word:
      return mean
    elif word > wordlist[mean]:
      low = mean + 1
    else:
      up = mean - 1

  return -1

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("python3 search.py <word>")
    exit()

  word = sys.argv[1]
  words = get_words()
  words2 = get_words()

  t_search = timer()
  search_id = search(word, words)
  t_search = timer() - t_search

  print(search_id, str(t_search))
  if search_id >=0 :
    print("searched: ", words[search_id])

  t_sort = timer()
  words2.sort()
  t_sort = timer() - t_sort

  t_bsearch = timer()
  search_id = bin_search(word, words2)
  t_bsearch = timer() - t_bsearch
  print(search_id, str(t_bsearch), str(t_sort))
  
  if search_id >=0 :
    print("searched: ", words2[search_id])
