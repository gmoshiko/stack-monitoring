# Monitor-Stack

Monitor-Stack build on Vagrant & Docker.

## Description

in this stack you will find: 
* ELK Stack
* Grafana Dashboard
* Prometheus Server
* Graphite

everything will be provision using the stacktool.py included in this repo. 

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
git clone url
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

```
./stacktool.py -h
./stacktool.py status
which python
```

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