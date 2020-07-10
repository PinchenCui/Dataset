docker exec -i test-mysql mysql -uroot -ppinchen < init.sql
docker exec -i test-mysql chmod -R +rwx /tmp/Virus
docker exec -i test-mysql service ssh start
