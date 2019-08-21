#!/bin/bash
# sends POST request with custom variables to input webserver
curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
