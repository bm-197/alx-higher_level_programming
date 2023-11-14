#!/usr/bin/node

if (isNaN(process.argv[2])) {
    console.log('Missing number of occurance');
    
} else {
    for ( const i = 0; i < process.argv[2]; i++) {
        console.log('C is fun');
    }
}
