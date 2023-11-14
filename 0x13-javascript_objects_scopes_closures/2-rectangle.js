#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
        if (w === 0 ||h === 0) {
            this.w = w;
            this.h = h;
        }
    }  
};
