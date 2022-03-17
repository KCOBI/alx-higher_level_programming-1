#!/bin/bash
# this will add custom header
curl -X GET $1 -H "X-School-User-Id: 98"
