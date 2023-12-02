#!/bin/bash
#script that takes in a URL

curl -sI "$1" | grep -i content-length | wc -c