#!/bin/bash
#script that takes in a URL

curl -so /deb/nul -w '%{size_download}\n' "$1"