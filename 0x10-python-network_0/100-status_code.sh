#!/bin/bash
# this only show the status code
curl -s -o /dev/null -sw "%{http_code}" "$1"
