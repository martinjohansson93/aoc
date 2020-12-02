const { readFileSync } = require("fs");

const input = readFileSync("input.txt")
  .toString()
  .replace(/\r\n/g, "\n")
  .split("\n");

input.forEach((a) => {
  input.forEach((b) => {
    parseInt(a) + parseInt(b) === 2020
      ? console.log(parseInt(a) * parseInt(b))
      : null;
  });
});

input.forEach((a) => {
  input.forEach((b) => {
    input.forEach((c) => {
      parseInt(a) + parseInt(b) + parseInt(c) === 2020
        ? console.log(parseInt(a) * parseInt(b) * parseInt(c))
        : null;
    });
  });
});
