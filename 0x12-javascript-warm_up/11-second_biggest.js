#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const args = process.argv.map(Number)
      .slice(2, process.argv.length)
      .sort((a, b) => b - ba);
    console.log(args[1]);
  }