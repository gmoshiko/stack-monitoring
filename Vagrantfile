## Script to run after docker init ##
$script = <<-SCRIPT
apt update
docker swarm init 
git clone https://github.com/vegasbrianc/prometheus.git 
git clone https://github.com/deviantony/docker-elk.git
cp /tmp/docker-prom-st.yml prometheus/
cd prometheus
HOSTNAME=$(hostname) docker stack deploy -c docker-prom-st.yml prom
sleep 10
cd /home/vagrant/docker-elk
docker stack deploy -c docker-stack.yml elk
sleep 10
SCRIPT

## Message 
$msg = <<MSG
------------------------------------------------------
Local Monitor Stack, accessible at 127.0.0.1 || localhost

URLS:
 - Kibana Dashboard  - http://localhost:9005
 - ElasticSearch     - http://localhost:9006
 - Graphite  - http://localhost:9003
 - Prometheus Server  - http://localhost:9001
 - Grafana Dashboard  - http://localhost:9000

Please wait for a few minuts, and run stacktool.py status to see everything is working as expected.
You can use stacktool.py tool to control everything in the stack.

------------------------------------------------------
MSG

## Using Ubuntu with 4 cpu and 4 memory
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provider "virtualbox" do |v|
    v.name = "Stack_monitoring"
    v.memory = 4096
    v.cpus = 4
  end
  config.vm.network "forwarded_port", guest: 3000, host: 9000
  config.vm.network "forwarded_port", guest: 9090, host: 9001
  config.vm.network "forwarded_port", guest: 81, host: 9003
  config.vm.network "forwarded_port", guest: 5601, host: 9005
  config.vm.network "forwarded_port", guest: 9200, host: 9006
  ####### Provision #######
  config.vm.provision "docker" do |docker|
  config.vm.provision "file", source: "docker-stack-prometheus.yml", destination: "/tmp/docker-prom-st.yml"
  config.vm.provision "shell", inline: $script
    docker.build_image "/vagrant",
      args: "-t kaltura/graphite"
    docker.run "graphite",
      image: "kaltura/graphite:latest",
      args: "-p 81:81 -p 2003-2004:2003-2004 -p 2023-2024:2023-2024 -p 8125:8125/udp -p 8126:8126"
  config.vm.post_up_message = $msg
  end
end
