const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{2,}/g);

const mandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
const optionalFields = ["cid"];

const includesAllMandatoryFields = (passport) => {
  let valid = true;
  const passportWithSpaces = passport.replace(/(\r\n|\n|\r)/gm, " ");
  if (passportWithSpaces.split(" ").length < 7) return false;
  mandatoryFields.forEach((field) => {
    if (!passportWithSpaces.includes(`${field}:`)) valid = false;
  });
  return valid;
};

const input = readInput();
let validPassports = 0,
  invalidPassports = 0;

input.forEach((passport) => {
  includesAllMandatoryFields(passport)
    ? (validPassports += 1)
    : (invalidPassports += 1);
});

console.log(`🚀 Valid Passports: ${validPassports}`);
console.log(`🚀 Invalid Passports: ${invalidPassports}`);
