#!/usr/bin/node
/*
    Print a square with the character #

    The size of the square must be the first argument
    of the program.
    */

if (process.argv.length <= 2) {
	process.stderr.write("Missing argument\n");
	process.stderr.write("Usage: ./1-print_square.js <size>\n");
	process.stderr.write("Example: ./1-print_square.js 8\n");
	process.exit(1)
}

const size = parseInt(process.argv[2], 10);
let row = 0;

while (row < size) {
	let column = 0;
	while (column < size) {
		process.stdout.write("#");
		column++;
	}
	process.stdout.write("\n");
	row++;
}
