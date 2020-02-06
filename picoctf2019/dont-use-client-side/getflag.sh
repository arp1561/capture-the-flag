#!/bin/bash

cat index.html | head -n 20 | tail -n 8 | sort -n
#cat index.html | head -n 20 | tail -n 8 | cut -d "'" -f2 | tr -d '\n' 
