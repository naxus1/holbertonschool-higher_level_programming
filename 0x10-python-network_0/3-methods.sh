#!/bin/bash
 #Displays the size of the body of the response
curl -sI $1 | head -4 | tail -1 | cut -d":" -f2 | sed 's/ //'
