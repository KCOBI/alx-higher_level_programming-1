#!/bin/bash
# this only show the status code
curl $1 -sI | grep -i HTTP | awk '{print $2}'
