const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt").toString().replace(/\r\n/g, "\n").split("\n");

const input = readInput();
const inputWidth = input[0].length;
let yCoordinate = 0;
let trees = 0;
input.forEach((row) => {
  row[yCoordinate] === "#" ? (trees += 1) : 0;
  yCoordinate =
    yCoordinate + 3 >= inputWidth
      ? yCoordinate + 3 - inputWidth
      : yCoordinate + 3;
});

console.log(`🚀 Trees: ${trees}`);
