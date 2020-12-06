const { readFileSync } = require("fs");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{2,}/g);

const mandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

const validationFields = {
  byr: (x) => 1920 <= x && x <= 2002,
  iyr: (x) => 2010 <= x && x <= 2020,
  eyr: (x) => 2020 <= x && x <= 2030,
  hgt: (x) => {
    if (x.includes("cm")) {
      return (
        150 <= parseInt(x.split("cm")[0]) && parseInt(x.split("cm")[0]) <= 193
      );
    } else if (x.includes("in")) {
      return (
        59 <= parseInt(x.split("in")[0]) && parseInt(x.split("in")[0]) <= 76
      );
    }
    return false;
  },
  ecl: (x) => ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(x),
  hcl: (x) => {
    let valid = true;
    const firstChar = x[0];
    const rest = x.substring(1);
    firstChar === "#"
      ? rest.length === 6
        ? rest.split("").forEach((y) => {
            if (
              ![
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
              ].includes(y)
            )
              valid = false;
          })
        : (valid = false)
      : (valid = false);
    return valid;
  },
  pid: (x) => {
    let valid = true;
    x.split("").length === 9
      ? x.split("").forEach((y) => {
          if (!["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].includes(y))
            valid = false;
        })
      : (valid = false);
    return valid;
  },
  cid: (x) => true,
};

const includesAllMandatoryFields = (passport) => {
  let valid = true;

  mandatoryFields.forEach((field) => {
    if (!passport.includes(`${field}:`)) valid = false;
  });
  return valid;
};

const validateFields = (passport) => {
  let valid = true;
  validationFields;
  passport.split(" ").forEach((field) => {
    if (!validationFields[field.substring(0, 3)](field.split(":")[1]))
      valid = false;
  });
  return valid;
};

const input = readInput();
let validPassports = 0,
  invalidPassports = 0;

input.forEach((passport) => {
  const passportWithSpaces = passport.replace(/(\r\n|\n|\r)/gm, " ");
  if (includesAllMandatoryFields(passportWithSpaces)) {
    const valid = validateFields(passportWithSpaces);
    valid ? (validPassports += 1) : (invalidPassports += 1);
  } else {
    invalidPassports += 1;
  }
});

console.log(`🚀 Valid Passports: ${validPassports}`);
console.log(`🚀 Invalid Passports: ${invalidPassports}`);
