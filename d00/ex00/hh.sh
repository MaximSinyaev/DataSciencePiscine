#!/bin/sh
# Ask headhunter API for reliable vacancies
#{1} - vacancy name

if [ $# -eq 1 ]; then
	vacancy=$( echo $1 | tr ' ' '-')
	curl -k "https://api.hh.ru/vacancies?text=${vacancy}&page=0" | json_pp > hh.json
else
	echo "Vacancy name must contain at least 1 sign"
fi
