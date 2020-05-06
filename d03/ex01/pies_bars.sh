#!/usr/bin/env bash
echo "@ money, not money
2018 200.45 180.2
2017 110.45 92.9
2016 77.89 92.9
2015 66.2 55.1
2014 760.00 720.3" > ex.dat
termgraph ex.dat --color {yellow,magenta}
rm -f ex.dat