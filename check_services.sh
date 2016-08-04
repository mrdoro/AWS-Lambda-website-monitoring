#!/bin/bash
APACHESTS=`sudo service httpd status | rev | cut -c4-10 | rev`
SQLSTAT=`sudo service mysqld status | rev | cut -c4-10 | rev`
if [ "$APACHESTS" = "running" ]; then
	echo pętla1 apache is running >> /tmp/logstat.log
	if [ "$SQLSTAT" = "running" ]; then
		echo pętla2 mysql is running >> /tmp/logstat.log
	else
		echo pętla2 else1 restart obydwu >> /tmp/logstat.log
		sudo service mysqld restart
		sudo service httpd restart
	fi
else
	if [ "$SQLSTAT" = "running" ]; then
		echo pętla3 mysql is running restart http >> /tmp/logstat.log
    	sudo service httpd restart
	else
		echo petla3 else1 czyli restart obydwi >> /tmp/logstat.log
		sudo service mysqld restart
		sudo service httpd restart
	fi
fi
