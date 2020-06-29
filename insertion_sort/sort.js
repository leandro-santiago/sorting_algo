const fs = require('fs')

function get_words() {
  const fname = "../dataset/words_10000.txt";

  return fs.readFileSync(fname, 'utf8').split('\n').filter(Boolean);
}

// O(n^2) - Best case O(n)
function insertion_sort(list) {
  for (let i = 1; i < list.length; i++) {
    let key = list[i];
    let j = i - 1;

    while ((j >= 0) && (list[j] > key)) {
      list[j+1] = list[j];
      j--;
    }

    list[j + 1] = key;
  }
}

let wordlist = get_words();
let wordlist2 = get_words();

console.log(wordlist);

var tsort = process.hrtime.bigint();
insertion_sort(wordlist);
tsort = (process.hrtime.bigint() - tsort);

console.log(wordlist);

var tsort2 = process.hrtime.bigint();
wordlist2.sort();
tsort2 = (process.hrtime.bigint() - tsort2);

console.log(wordlist2);
console.log(tsort, tsort2);
