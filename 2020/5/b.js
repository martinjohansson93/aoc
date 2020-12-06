const { readFileSync } = require("fs");
const { clone } = require("ramda");

const readInput = () =>
  readFileSync("input.txt")
    .toString()
    .replace(/\n\r/g, "\n")
    .replace(/\r/g, "\n")
    .split(/\n{1,}/g);

const firstRow = 0;
const lastRow = 127;

var allRows = [];
for (var i = firstRow; i <= lastRow; i++) {
  allRows.push(i);
}

const firstColumn = 0;
const lastColumn = 7;

var allColumns = [];
for (var i = firstColumn; i <= lastColumn; i++) {
  allColumns.push(i);
}

const getRowRecursive = (chars, remainingRows) => {
  if (!chars.length) {
    return remainingRows[0];
  }
  const char = chars.shift();

  if (char === "F") {
    return getRowRecursive(
      chars,
      remainingRows.slice(0, Math.ceil(remainingRows.length / 2))
    );
  } else if (char === "B") {
    return getRowRecursive(
      chars,
      remainingRows.slice(
        Math.ceil(remainingRows.length / 2),
        remainingRows.length
      )
    );
  }
};

const getColumnRecursive = (chars, remainingColumns) => {
  if (!chars.length) {
    return remainingColumns[0];
  }
  const char = chars.shift();

  if (char === "L") {
    return getColumnRecursive(
      chars,
      remainingColumns.slice(0, Math.ceil(remainingColumns.length / 2))
    );
  } else if (char === "R") {
    return getColumnRecursive(
      chars,
      remainingColumns.slice(
        Math.ceil(remainingColumns.length / 2),
        remainingColumns.length
      )
    );
  }
};

const input = readInput();
const seatIds = [];
input.forEach((boardingpass) => {
  const row = getRowRecursive(
    boardingpass.substring(0, 7).split(""),
    clone(allRows)
  );
  const column = getColumnRecursive(
    boardingpass.substring(7, 10).split(""),
    clone(allColumns)
  );
  seatIds.push(row * 8 + column);
});
seatIds.sort((a, b) => a - b);
try {
  seatIds.forEach((seat, i) => {
    if (!(seat + 2 === seatIds[i + 2])) {
      console.log("🚀 Answer: ", seat + 2);
      throw new Error("hahahah");
    }
  });
} catch (e) {}
