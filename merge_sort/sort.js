const fs = require("fs");

function get_words(){
  const fname = "../dataset/words_320139.txt";

  return fs.readFileSync(fname, 'utf8').split("\n").filter(Boolean);
}

// O(n log(n))
function merge_sort(list, low, up) {
  if (low < up) {
    let center = (low + up) >> 1; // (low + up) / 2
    merge_sort(list, low, center);
    merge_sort(list, center + 1, up);
    merge(list, low, center, up);
  }
}

function merge(list, low, center, up) {
  let low1 = low;
  let low2 = center + 1;
  let aux_list = [];

  while ((low1 <= center) && (low2 <= up) ){
    if (list[low1] < list[low2]) {
      aux_list.push(list[low1]);
      low1++;
    } else {
      aux_list.push(list[low2]);
      low2++;
    }
  }

  while (low1 <= center) {
    aux_list.push(list[low1]);
    low1++;
  }

  while (low2 <= up) {
    aux_list.push(list[low2]);
    low2++;
  }

  for (let i = 0; i < aux_list.length; i++) {
    list[low + i] = aux_list[i];
  }

}

let wordlist = get_words();
let wordlist2 = get_words();

var tsort = process.hrtime.bigint();
merge_sort(wordlist, 0, wordlist.length - 1);
tsort = process.hrtime.bigint() - tsort;

var tsort2 = process.hrtime.bigint();
wordlist2.sort();
tsort2 = process.hrtime.bigint() - tsort2;

console.log(wordlist);
console.log(wordlist2);
console.log(tsort, tsort2);
