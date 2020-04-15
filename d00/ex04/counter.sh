#!/bin/sh
# Counts uniq names in dataset
if [ $# -eq 1 ]; then
	rm -f hh_uniq_positions.csv
	echo \"name\",\"count\" > hh_uniq_positions.csv
	sed -n '2,$p'  ../ex03/hh_positions.csv  | cut -d, -f3 | uniq -ic | sort -ur -k1 | sed -e 's/^ *//g' -e 's/\([0-9]\+\) \(".*\)/\2,\1/g' >> hh_uniq_positions.csv
fi
