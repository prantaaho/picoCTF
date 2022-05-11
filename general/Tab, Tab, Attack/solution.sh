#!/bin/bash

unzip -oj Addadshashanammu.zip
strings fang-of-haynekhtnamet | grep -oe 'picoCTF{.*}'
