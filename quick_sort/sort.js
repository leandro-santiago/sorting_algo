const fs = require('fs');

function get_words() {
  const fname = "../dataset/words_320139.txt";

  return fs.readFileSync(fname, 'utf8').split("\n").filter(Boolean);
}

// O(n log(n))
function quick_sort(list, low, up) {
  if (low < up) {
    let pivot = partition(list, low, up);
    quick_sort(list, low, pivot);
    quick_sort(list, pivot + 1, up);
  }
}

function partition(list, low, up) {
  let center = (up - low) >> 1; // (up - low)/2
  let pivot = list[low + center];
  let i = low;
  let j = up;
  let aux = "";

  while (true) {
    while (list[i] < pivot) {
      i++;
    }

    while (list[j] > pivot) {
      j--;
    }

    if (i >= j) return j;

    aux = list[i];
    list[i] = list[j];
    list[j] = aux;
  }
}

let wordlist = get_words();
let wordlist2 = get_words();

var tsort = process.hrtime.bigint();
quick_sort(wordlist, 0, wordlist.length - 1);
tsort = process.hrtime.bigint() - tsort;

var tsort2 = process.hrtime.bigint();
wordlist2.sort();
tsort2 = process.hrtime.bigint() - tsort2;

console.log(wordlist);
console.log(wordlist2);
console.log(tsort, tsort2);
