#!/bin/sh
mysqlimport -u root rahasto `pwd`/$1 --fields-terminated-by=',' --columns=fund,rating,currency,nav,day1,month3,month6,year1,year3,date --local
