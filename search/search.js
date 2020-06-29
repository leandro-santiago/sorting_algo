const fs = require('fs');

// O(n)
function search(item, list) {
  for (let i = 0; i < list.length; i++) {
    if (list[i] == item) {
      return i;
    }
  }

  return -1;
}

// O(log(n))
function bin_search(item, list) {
  let low = 0;
  let up = list.length - 1;

  while (low < up) {
    let mean = (low + up) >> 1; // (low + up)/2

    if (list[mean] == item) {
      return mean;
    } else if (item > list[mean]) {
      low = mean + 1;
    } else {
      up = mean - 1;
    }
  }

  return -1;
}

if (process.argv.length != 3) {
  console.log("node search.js <word>");
  return;
}

const fname = '../dataset/words_320139.txt';
let wordlist = fs.readFileSync(fname, 'utf8').split('\n').filter(Boolean);
let wordlist2 = fs.readFileSync(fname, 'utf8').split('\n').filter(Boolean);
let word = process.argv[2];

let t_search = process.hrtime.bigint();
let index = search(word, wordlist);
t_search = process.hrtime.bigint() - t_search;

let t_sort = process.hrtime.bigint();
wordlist2.sort();
t_sort = process.hrtime.bigint() - t_sort;

let t_bsearch = process.hrtime.bigint();
let index2 = bin_search(word, wordlist2);
t_bsearch = process.hrtime.bigint() - t_bsearch;

console.log(index, wordlist[index], t_search);
console.log(index2, wordlist2[index2], t_bsearch, t_sort);
