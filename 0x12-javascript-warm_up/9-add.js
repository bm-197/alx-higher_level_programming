#!/usr/bin/node

const num = Number(process.argv[2]);

function factorial (num) {

	if (num > 1)
		return (num * factorial(num - 1));
	else
		return 1;
}
