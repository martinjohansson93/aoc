const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt").toString().replace(/\r\n/g, "\n").split("\n");

const isPasswordValid = (policy) => {
  const policyParts = policy.split(" ");
  const firstAndSecondPos = policyParts[0].split("-");
  const firstPos = firstAndSecondPos[0] - 1;
  const secondPos = firstAndSecondPos[1] - 1;

  return (
    (policyParts[2][firstPos] === policyParts[1][0] ||
      policyParts[2][secondPos] === policyParts[1][0]) &&
    !(
      policyParts[2][firstPos] === policyParts[1][0] &&
      policyParts[2][secondPos] === policyParts[1][0]
    )
  );
};

const input = readInput();

let validPasswords = 0;
input.forEach((policy) => {
  if (isPasswordValid(policy)) validPasswords++;
});
console.log(`🚀 validPasswords: ${validPasswords}`);
