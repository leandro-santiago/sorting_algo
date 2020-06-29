import 'dart:io';

List<String> get_words() {
  var fname = "../dataset/words_320139.txt";
  File fd = new File(fname);  
  return fd.readAsStringSync().split("\n").where((el) => el.isNotEmpty).toList();
}

// O(n)
int search(String item, List<String> list) {
  for (int i = 0; i < list.length; i++) {
    if (list[i] == item) {
      return i;
    }
  }

  return -1;
}

// O(log(n))
int bin_search(String item, List<String> list) {
  int low = 0;
  int up = list.length - 1;

  while (low < up) {
    int mean = (low + up) >> 1; // (low + up)/2

    if (list[mean] == item) {
      return mean;
    } else if (list[mean].compareTo(item) < 0) {
      low = mean + 1;
    } else {
      up = mean - 1;
    }
  }

  return -1;
}


void main(List<String> argv) {
  
  if (argv.length != 1) {
    print("dart search.dart <word>");
    return;
  }

  String word = argv[0];
  List wordlist = get_words();
  List wordlist2 = get_words();

  Stopwatch timer1 = new Stopwatch();

  timer1.start();
  int index = search(word, wordlist);
  timer1.stop();

  Stopwatch timer = new Stopwatch();
  timer.start();
  wordlist2.sort();
  timer.stop();

  Stopwatch timer2 = new Stopwatch();
  timer2.start();
  int index2 = bin_search(word, wordlist2);
  timer2.stop();

  print("${index}, ${timer1.elapsedMicroseconds}");
  if (index >= 0) { 
    print("${wordlist[index]}");
  }

  print("${index2}, ${timer2.elapsedMicroseconds}, ${timer.elapsedMicroseconds}");
  if (index >= 0) { 
    print("${wordlist2[index2]}");
  }

}