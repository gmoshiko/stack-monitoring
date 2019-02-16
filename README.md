# Monitor-Stack

Monitor-Stack build on Vagrant & Docker.

## Description

THIS IS FOR DEMO ONLY.
it can be done in many ways. for exmaple you can use ansible_local with vagrant.  
stacktool was build for internal use to check the stack while i was builing it.  
the stacktool is only checking some response code and regex. you can edit it and add  
more tests as needed.  

in this stack you will find: 
* ELK Stack
* Grafana Dashboard
* Prometheus Server
* Graphite

everything will be provision using the stacktool.py included in this repo.  
The stack build on top Ubuntu VM using Vagrant to provision, docker & Docker Swarm
to run the services.  
after installing the stack you can access it via http://localhost:port 

## Getting Started

Before starting, please install the dependencies

### Dependencies

* Vagrant - https://www.vagrantup.com/downloads.html
* Python3.x - https://www.python.org/downloads/
* VirtualBox - https://www.virtualbox.org/wiki/Downloads
* Install requirements.txt (python requests)

```
pip install requirements.txt
or
pip install requests
```

### Installing & Executing program

to start working with the stack, you simply need to run stacktool.py up

```
git clone https://github.com/gmoshiko/stack-monitoring
cd stack-monitoring
chmod +x stacktool.py
./stacktool.py up
```

## Help

* check the interpreter on the script
* grafana user|password admin|foobar
* ports:  
9000 -> Grafana Dashboard  
9001 -> Prometheus Server  
9003 -> Graphite  
9005 -> Kibana Dashboard  
9006 -> ElasticSearch  

in the end of the provision, you will get a message with everything you need.  

```
./stacktool.py -h
./stacktool.py status
which python
```

## Stacktool

Stacktool is build for maintain, and monitor the stack.  
for example you can send any docker command to the docker driver inside the VM with just adding '--cmd'

```
./stacktool.py docker --cmd ps
```

it can do even more advance commands like that:

```
./stacktool.py docker --cmd 'logs 60cbbccec46d'
```
Options: 
* up - bring the stack up.
* purge - deleting the stack.
* status - healthcheck the stack.
* docker - using for docker commands.
* vagrant - using for vagrant commands.

## Authors

Moshiko Gueta gmoshiko@gmail.com

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [docker-elk](https://github.com/deviantony/docker-elk)
* [docker-graphite-statsd](https://github.com/hopsoft/docker-graphite-statsd)
* [docker-prometheus](https://github.com/vegasbrianc/prometheus)

## Reference

* [prometheus-api](https://prometheus.io/docs/prometheus/latest/querying/api/)
* [grafana-api](http://docs.grafana.org/http_api/auth/)
* [vagrant-docker](https://www.vagrantup.com/docs/provisioning/docker.html)
