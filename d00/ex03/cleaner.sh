#!/bin/sh
# pretify name column in hh data
if [ $# -eq 1 ]; then
	rm -f hh_positions.csv
	cat $1 | sed -e 's/[Dd]ata [Ss]cientist//g' -e 's/,"",/,"Data Scientist",/g' -e 's@\(,".*\)[/]\(.*",\)@\1\2@g' -e 's/[()]//g' -e 's/\("[ ]\+\)\|\([ ]\+"\)/"/g' -e 's/[ ]\+\|, / /g' > hh_positions.csv
fi
