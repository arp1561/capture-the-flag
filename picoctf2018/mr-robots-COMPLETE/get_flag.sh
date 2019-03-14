#!/bin/bash
curl -s "http://2018shell.picoctf.com:15298/c4075.html" | grep -oE "picoCTF{.*}" --color=none
