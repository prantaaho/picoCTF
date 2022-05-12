#!/bin/bash

# Download the document
wget https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm

# unzip
unzip "Forensics is fun.pptm"

# Get flag
tr -d ' ' < ppt/slideMasters/hidden | base64 -d 2> /dev/null
