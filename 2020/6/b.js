const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{2,}/g);

const input = readInput();

let answeredQuestions = 0;
input.forEach((answersGroup) => {
  const answersInGroup = answersGroup.split(/\n/g);
  let answerAsArray = answersInGroup.pop().split("");
  answersInGroup.forEach((ans) => {
    answerAsArray = answerAsArray.filter((x) => ans.split("").includes(x));
  });
  answeredQuestions += answerAsArray.length;
});

console.log(`🚀 Answered questions: ${answeredQuestions}`);
