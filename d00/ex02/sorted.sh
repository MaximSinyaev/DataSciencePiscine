#!/bin/sh
# Sort .csv data by 1st and 4th columns
if [ $# -eq 1 ] && [ -e $1 ]; then
	rm -f hh_sorted.csv
	cat $1 | sed -n "1p" > hh_sorted.csv
	cat $1 | sed -n '2,$p' | sort -t, -k1,2  >> hh_sorted.csv
fi
