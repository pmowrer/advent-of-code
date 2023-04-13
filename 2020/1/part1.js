const { readFileSync } = require('fs');
const input = readFileSync('./input1').toString().split('\n');
const hash = {};
let answer;
let i = 0;

while (!answer && i < input.length) {
  const expense = Number(input[i]);
  const remainder = 2020 - expense;
  
  if (hash[remainder]) {
    answer = expense * remainder;
  } else {
    hash[expense] = expense;
  }

  i++;
}

console.log('answer', answer);
