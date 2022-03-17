#!/bin/bash
#this will show the allowd responses
curl -X OPTIONS $1 -sI | grep -i Content-Length | awk '{print $2 $3 $4 $5}'
