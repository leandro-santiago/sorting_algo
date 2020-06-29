import 'dart:io';
import 'dart:core';

List<String> get_words() {
  String fname = "../dataset/words_320139.txt";
  File fd = new File(fname);

  return fd.readAsStringSync().split("\n").where((el) => el.isNotEmpty).toList();
}

// O(n log(n))
void merge_sort(List<String> list, int low, int up) {
  if (low < up) {
    int center = (low + up) >> 1; // (low + up) / 2
    merge_sort(list, low, center);
    merge_sort(list, center + 1, up);
    merge(list, low, center, up);
  }
}

void merge(List<String> list, int low, int center, int up) {
  int low1 = low;
  int low2 = center + 1;
  List<String> aux_list = [];

  while ((low1 <= center) && (low2 <= up)) {
    if (list[low1].compareTo(list[low2]) < 0) {
      aux_list.add(list[low1]);
      low1++;
    } else {
      aux_list.add(list[low2]);
      low2++;
    }
  }

  while (low1 <= center) {
    aux_list.add(list[low1]);
    low1++;
  }

  while (low2 <= up) {
    aux_list.add(list[low2]);
    low2++;
  }

  for (int i = 0; i < aux_list.length; i++) {
    list[low + i] = aux_list[i];
  }

}

void main() {
  List<String> wordlist = get_words();
  List<String> wordlist2 = get_words();

  Stopwatch tsort = new Stopwatch();
  Stopwatch tsort2 = new Stopwatch();

  tsort.start();
  merge_sort(wordlist, 0, wordlist.length - 1);
  tsort.stop();
  
  tsort2.start();
  wordlist2.sort();
  tsort2.stop();

  print(wordlist);
  print(wordlist2);
  print("${tsort.elapsedMicroseconds}, ${tsort2.elapsedMicroseconds}");

}