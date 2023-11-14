#!/usr/bin/node
const len = process.argv.length;
const min = process.argv[2];

for (let i = 3; i < len; i++) {
    if ( process.argv[i] < min) {
        min = process.argv[i];
    }
}
console.log(min);