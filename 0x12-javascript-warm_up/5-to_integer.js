#!/usr/bin/node
const val = Math.floor(Number(process.argv[2]));
console.log(isNaN(val) ? 'Not a number' : 'My number: ${val}');
