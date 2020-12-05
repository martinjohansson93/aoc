const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt").toString().replace(/\r\n/g, "\n").split("\n");

const isPasswordValid = (policy) => {
  const policyParts = policy.split(" ");
  const minAndMax = policyParts[0].split("-");
  const occurences = policyParts[2].split(policyParts[1][0]).length - 1;

  return occurences >= minAndMax[0] && occurences <= minAndMax[1];
};

const input = readInput();

let validPasswords = 0;
input.forEach((policy) => {
  if (isPasswordValid(policy)) validPasswords++;
});
console.log(`🚀 validPasswords: ${validPasswords}`);
