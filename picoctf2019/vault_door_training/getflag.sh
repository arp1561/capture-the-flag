#!/bin/bash

var=$(cat VaultDoorTraining.java | tail -n 3 | head -n 1 | cut -d '"' -f2)

echo "picoCTF{${var}}"
