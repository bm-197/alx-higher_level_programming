#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
        if (w === 0 ||h === 0) {
            this.w = w;
            this.h = h;
        }
    }
    print () {
        for (let i = 0; i < this.h; i++) {
            console.log('X'.repeat(this.w));
        }
    }
    rotate () {
        [this.w, this.h] = [this.h, this.w];
    }
    double () {
        this.w = 2 * this.w;
        this.h = 2 * this.h;
    }
};