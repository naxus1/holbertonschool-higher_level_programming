#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
curl -sI "$1" | grep Allow | cut -d ":" -f2 | sed -e 's/^[ \t]*//'
