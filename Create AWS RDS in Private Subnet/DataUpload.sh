#!/bin/bash
echo "Hello"

unzip names.zip -d names

cd names

for f in *.txt
do
s=`echo $f | cut -c 4-7`
sed -i "s/$/,$s/" $f
done

cat *.txt > ssanames.txt

mysqlimport --local --user=G36182176 --password=providepassword --host=g36182176-mysql.cv0flyvrlwcj.us-east-2.rds.amazonaws.com
--fields-terminated-by=',' G36182176_ssanames ssanames.txt

