#!/bin/bash
# William Moody (@bmdyy)
# 30.11.2022
# Usage: ./data.sh N_THREADS

for i in {0..0}; do
	echo -en "$1\t"
	python3 dump.py $1 | grep -Eo '[0-9].[0-9]{6}' | tr '\n' '\t'
	echo -en "\n"
done
