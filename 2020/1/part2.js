const { readFileSync } = require('fs');
const input = readFileSync('./input1').toString().split('\n');
const hash = {};
const seen = [];
let answer;
let i = 0;

while (!answer && i < input.length) {
  const expense = Number(input[i]);
  const remainder = 2020 - expense;
  
  let j = 0;

  while (!answer && j < seen.length) {
    const remainder2 = remainder - seen[j];

    if (hash[remainder2]) {
      answer = expense * seen[j] * remainder2;
    }

    j++;
  }

  hash[expense] = expense;
  seen.push(expense);
  i++;
}

console.log('answer', answer);
