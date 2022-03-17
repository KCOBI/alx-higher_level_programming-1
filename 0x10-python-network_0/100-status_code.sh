#!/bin/bash
# this only show the status code
curl -s -o /dev/null -w "%{http_code}" $1
