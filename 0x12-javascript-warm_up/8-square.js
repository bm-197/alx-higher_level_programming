#!/usr/bin/node

if (!(isNaN(process.argv[2]))) {
    for (let i = 0; i < process.argv[2]; i++) {
        console.log('X'.repeat(process.argv[2]));
    }
} else {
    console.log('Missing size');
}
