import 'dart:io';
import 'dart:core';

List<String> get_words() {
  String fname = "../dataset/words_320139.txt";
  File fd = new File(fname);

  return fd.readAsStringSync().split("\n").where((el) => el.isNotEmpty).toList();
}

// O(n log(n))
void quick_sort(List<String> list, int low, int up) {
  if (low < up) {
    int pivot = partition(list, low, up);
    quick_sort(list, low, pivot);
    quick_sort(list, pivot+1, up);
  }
}

int partition(List<String> list, int low, int up) {
  int center = (up - low) >> 1; // (up - low)/2
  String pivot = list[low + center];
  int i = low;
  int j = up;
  String aux = "";

  while (true) {
    while (list[i].compareTo(pivot) < 0) {
      i++;
    }

    while (list[j].compareTo(pivot) > 0) {
      j--;
    }

    if (i >= j) return j;

    aux = list[i];
    list[i] = list[j];
    list[j] = aux;

  }

}

void main() {
  List wordlist = get_words();
  List wordlist2 = get_words();

  Stopwatch tsort = new Stopwatch();
  Stopwatch tsort2 = new Stopwatch();

  tsort.start();
  quick_sort(wordlist, 0, wordlist.length - 1);
  tsort.stop();
  
  tsort2.start();
  wordlist2.sort();
  tsort2.stop();
  String last = wordlist[wordlist.length-1];
  String last2 = wordlist2[wordlist2.length-1];

  print("${wordlist[0]},${last}");
  print("${wordlist2[0]},${last2}");
  print("${tsort.elapsedMicroseconds}, ${tsort2.elapsedMicroseconds}");

}