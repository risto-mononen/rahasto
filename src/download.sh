#!/bin/sh

for TYPE in 4 3 9 1 2
do
	curl "http://www.kauppalehti.fi/5/i/porssi/rahastot/index.jsp?fcomid=&type=$TYPE&class=&N%E4yt%E4.x=29&N%E4yt%E4.y=6&N%E4yt%E4=N%E4yt%E4" > $TYPE`date +%F`.html
done
