#!/bin/sh
mysqlimport -u root rahasto `pwd`/$1 --fields-terminated-by=','
