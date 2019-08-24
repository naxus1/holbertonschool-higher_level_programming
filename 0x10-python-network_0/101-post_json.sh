#!/bin/bash
# get status code
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
