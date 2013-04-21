#!/bin/sh
mysqlimport -u root rahasto `pwd`/$1 --fields-terminated-by=',' --columns=rahasto,rating,valuutta,arvo,pv1,kk3,kk6,v1,v3,pvm
