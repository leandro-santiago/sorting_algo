const fs = require('fs')

function get_words() {
  const fname = "../dataset/words_100000.txt";
  
  return fs.readFileSync(fname, 'utf8').split('\n').filter(Boolean);
}

function selection_sort(list) {
  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length; j++) {
      if (list[i] > list[j]) {
        let aux = list[i];
        list[i] = list[j];
        list[j] = aux;
      }
    }
  }
}

let wordlist = get_words();
let wordlist2 = get_words();

console.log(wordlist);

var tsort = process.hrtime.bigint();
selection_sort(wordlist);
tsort = (process.hrtime.bigint() - tsort);

var tsort2 = process.hrtime.bigint();
wordlist2.sort();
tsort2 = (process.hrtime.bigint() - tsort2);

console.log(wordlist);
console.log(wordlist2);
console.log(tsort, tsort2);
