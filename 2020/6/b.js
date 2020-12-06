const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{2,}/g);

const input = readInput();

let answeredQuestions = 0;
input.forEach((answers) => {
  const answer = answers.split(/\n/g);
  let array = answer.pop().split("");

  answer.forEach((ans) => {
    array = array.filter((x) => ans.split("").includes(x));
  });
  answeredQuestions += array.length;
});

console.log(`🚀 Answered questions: ${answeredQuestions}`);
