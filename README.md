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
docker network create --attachable -d overlay servernet
docker service create --network servernet --publish 8080:8080 --endpoint-mode vip --name simplehttpd --replicas 2 simple-python-server:latest
```

or without the service mesh
```
docker service create --network servernet --endpoint-mode dnsrr --name simplehttpd --replicas 2 simple-python-server:latest
```

And now use envoy to load-balance between them. Note, we use STRICT_DNS as the service discovery
policy in order to reflect changes in the service deployment immediately in envoy.

```
docker run --network servernet -ti --rm --name envoy -p 9901:9901 -p 10000:10000 -v $(pwd)/envoy.yaml:/etc/envoy/envoy.yaml  envoyproxy/envoy:v1.10.0
```



In a separate terminal, run
```
while true; do sleep 0.25; curl http://localhost:10000; done
```

And watch proper load balancing. 

```
server: dbcb82d6adf2
server: f2c9728a7952
server: f2c9728a7952
server: dbcb82d6adf2
server: dbcb82d6adf2
...
```

Also you might want to scale up or down:

```
docker service scale simplehttpd=3
```

Output changes to:
```
server: dbcb82d6adf2
server: f2c9728a7952
server: 0bffaf7733a9  <--- new instance
server: dbcb82d6adf2
server: f2c9728a7952
server: 0bffaf7733a9
server: 0bffaf7733a9
server: dbcb82d6adf2
server: f2c9728a7952
server: 0bffaf7733a9
...
```

Finally, remove by:
```
docker service rm simplehttpd
docker network rm servernet
```
