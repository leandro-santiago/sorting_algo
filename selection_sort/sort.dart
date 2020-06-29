import 'dart:io';
import 'dart:core';

List<String> get_words() {
  String fname = "../dataset/words_10000.txt";
  File fd = new File(fname);
  return fd.readAsStringSync().split("\n").where((el) => el.isNotEmpty).toList();
}

void selection_sort(List<String> list) {
  for (int i = 0; i < list.length; i++) {
    for (int j = i+1; j < list.length; j++) {
      if (list[i].compareTo(list[j]) > 0) {
        var aux = list[i];
        list[i] = list[j];
        list[j] = aux;
      }
    }
  }
}

void main() {
  List wordlist = get_words();
  List wordlist2 = get_words();

  print(wordlist);
  Stopwatch timer1 = new Stopwatch();
  Stopwatch timer2 = new Stopwatch();

  timer1.start();
  selection_sort(wordlist);
  timer1.stop();

  timer2.start();
  wordlist2.sort();
  timer2.stop();

  print(wordlist);
  print(wordlist2);
  print("${timer1.elapsedMicroseconds}, ${timer2.elapsedMicroseconds}");
}