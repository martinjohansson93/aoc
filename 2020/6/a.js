const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{2,}/g);

const input = readInput();

let answeredQuestions = 0;
input.forEach((answer) => {
  answeredQuestions += new Set(answer.replace(/\n/g, "").split("")).size;
});

console.log(`🚀 Answered questions: ${answeredQuestions}`);
