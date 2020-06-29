import 'dart:io';
import 'dart:core';

List<String> get_words() {
  String fname = "../dataset/words_10000.txt";
  File fd = new File(fname);

  return fd.readAsStringSync().split("\n").where((el) => el.isNotEmpty).toList();
}

// O(n^2) - Best case O(n)
void insertion_sort(List<String> list) {
  for (int i = 1; i < list.length; i++) {
    var key = list[i];
    int j = i - 1;

    while ((j >= 0) && (list[j].compareTo(key) > 0)) {
      list[j+1] = list[j];
      j--;
    }

    list[j + 1] = key;
  }
}

void main() {
  List wordlist = get_words();
  List wordlist2 = get_words();

  Stopwatch tsort = new Stopwatch();  
  Stopwatch tsort2 = new Stopwatch();

  tsort.start();
  insertion_sort(wordlist);  
  tsort.stop();

  print(wordlist);

  tsort2.start();
  wordlist2.sort();  
  tsort2.stop();

  print(wordlist2);
  print("${tsort.elapsedMicroseconds}, ${tsort2.elapsedMicroseconds}");

}
