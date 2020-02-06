#!/bin/bash

phrase="bDNhcm5fdGgzX3IwcDM1"
inside=$(echo $phrase | base64 --decode)

echo "picoCTF{${inside}}"


