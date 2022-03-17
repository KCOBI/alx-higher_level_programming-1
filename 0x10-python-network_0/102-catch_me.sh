#!/bin/bash
# Send JSON post request
curl -d @"$1" -H "Content-Type: application/json" -X POST $2
