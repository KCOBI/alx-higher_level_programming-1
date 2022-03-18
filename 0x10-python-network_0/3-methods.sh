#!/bin/bash
#this will show the allowd responses
curl -s -i -X OPTIONS $1 | grep -i Allow | awk '{print $2 $3 $4 $5}'
