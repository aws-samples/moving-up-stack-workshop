docker run --name mysql -p 3306:3306 \
 -v `pwd`/init.sql:/data/application/init.sql \
 -e MYSQL_ROOT_PASSWORD=myAwesomePassword \
 -d mysql:8.0 --init-file /data/application/init.sql

docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=myAwesomePassword -d mysql:8.0
