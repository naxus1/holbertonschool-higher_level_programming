#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
curl -sI $1 -X "OPTIONS" | head -2 | tail -1 | cut -d":" -f2 | cut -c2-
