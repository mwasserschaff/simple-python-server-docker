# Simple Python 3 Web Server

build:
```
docker build -t simple-python-server:latest .
```

Run:
```
docker run -p 8080:8080 -it --rm --name myserver simple-python-server:latest
```

In a Swarm:
```
docker network create -d overlay servernet
docker service create --network servernet --publish 8080:8080 --endpoint-mode vip --name simplehttpd --replicas 2 simple-python-server:latest
```
