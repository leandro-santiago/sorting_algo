from timeit import default_timer as timer

def get_words():
  fname = "../dataset/words_320139.txt"
  wordlist = []

  with open(fname, "r") as fd:
    for line in fd:
      wordlist.append(line.strip())
  
  return wordlist

# O(n log(n))
def merge_sort(wordlist, low, up):
  if low < up:
    center = (low + up) >> 1 # (low + up)/2
    merge_sort(wordlist, low, center)
    merge_sort(wordlist, center + 1, up)
    merge(wordlist, low, center, up)

def merge(wordlist, low, center, up):
  low1 = low
  low2 = center + 1
  aux_list = []

  while (low1 <= center) and (low2 <= up):
    if wordlist[low1] < wordlist[low2]:
      aux_list.append(wordlist[low1])
      low1 = low1 + 1
    else:
      aux_list.append(wordlist[low2])
      low2 = low2 + 1
  
  while (low1 <= center):
    aux_list.append(wordlist[low1])
    low1 = low1 + 1
  
  while (low2 <= up):
    aux_list.append(wordlist[low2])
    low2 = low2 + 1
  
  for i in range(len(aux_list)):
    wordlist[low + i] = aux_list[i]


wordlist = get_words()
wordlist2 = get_words()

tsort = timer()
merge_sort(wordlist, 0, len(wordlist) - 1)
tsort = timer() - tsort

tsort2 = timer()
wordlist2.sort()
tsort2 = timer() - tsort2


print(wordlist[:10], wordlist[-10:])
print(wordlist2[:10], wordlist2[-10:])
print(tsort, tsort2)
