#!/bin/bash
# Displays the size of the body of the response
curl -s "$1" | wc -m
