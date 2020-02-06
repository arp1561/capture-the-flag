#!/bin/bash

cat index.html | grep "pico" | cut -d ":" -f2 | cut -d ' ' -f2 | tr -d '\n'
cat mycss.css | grep "flag" | cut -d ":" -f2 | cut -d ' ' -f2 | tr -d '\n'
cat myjs.js | grep "flag" | cut -d ":" -f2 | cut -d ' ' -f2 

