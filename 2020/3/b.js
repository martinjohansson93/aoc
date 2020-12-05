const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt").toString().replace(/\r\n/g, "\n").split("\n");

const traverse = (right, down) => {
  const input = readInput();
  const inputWidth = input[0].length;
  let yCoordinate = 0;
  let trees = 0;
  for (let i = 0; i < input.length; i += down) {
    input[i][yCoordinate] === "#" ? (trees += 1) : 0;
    yCoordinate =
      yCoordinate + right >= inputWidth
        ? yCoordinate + right - inputWidth
        : yCoordinate + right;
  }
  return trees;
};

const slopes = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2],
];
let answer = 1;
slopes.forEach((slope) => {
  answer *= traverse(slope[0], slope[1]);
});
console.log(`🚀 Answer: ${answer}`);
