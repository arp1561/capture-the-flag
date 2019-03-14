#!/bin/bash
curl -s "http://2018shell.picoctf.com:8420/" | head -n 20 | cut -d "'" -f2 | tac | head -n 8 | tr -d "\n"


