#!/usr/bin/python3.6

"""
Author: Moshiko Gueta
Description: A tool to control the monitor stack.
you need to give execute permission to the script with: 'chown +x stacktool.py'
./stacktool.py -h will help you with the rest. 
"""

class main:
    def __init__(self):
        self.promData = 'http://prometheus:9090'
        self.grafDash = 'container_cpu_usage_seconds_total'
        self.grafLog = '"isSignedIn":true,"id":1,"login":"admin","email":"admin@localhost"'
        self.promUp = '"job":"cadvisor"'

    def request_center(self, url, ext=False):
        import requests
        import re

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Got 200 Response code.")
                if ext is False:
                    return True
                if re.search(ext, response.text):
                    print("Found Regex")
                else:
                    print("Failed to find regex.")
                    return False
            else:
                print("not 200 response code")
                print(response.status_code, response.text)
                return False
            return True
        except:
            print("couldnt even send the request")
            return False

    def grafana_status(self):
        print("Checking Grafana Status")
        loginUrl = 'http://admin:foobar@localhost:9000/login'
        datasourceUrl = 'http://admin:foobar@localhost:9000/api/datasources'
        dashboardUrl = 'http://admin:foobar@localhost:9000/api/dashboards/uid/64nrElFmk'

        print("Trying to login Granfa")
        result = self.request_center(loginUrl, ext=self.grafLog)
        if result is False:
            print("Grafana: Not OK \n")
            return False

        print("Trying to get datasource prometheus")
        result = self.request_center(datasourceUrl, ext=self.promData)
        if result is False:
            print("Grafana: Not OK \n")
            return False

        print("Trying to get dashboard cpu parameter")
        result = self.request_center(dashboardUrl, ext=self.grafDash)
        if result is False:
            print("Grafana: Not OK \n")
            return False

        print("Grafana: OK \n")
        return True

    def prometheus_status(self):
        print("Checking Prometheus Status")
        queryUpUrl = 'http://localhost:9001/api/v1/query?query=up'

        result = self.request_center(queryUpUrl, ext=self.promUp)
        if result is False:
            print("Prometheus: Not OK \n")
            return False

        print("Prometheus: OK \n")
        return True

    def graphite_status(self):
        print("Checking Graphite Status")
        url = 'http://localhost:9003'

        result = self.request_center(url)
        if result is False:
            print("Graphit: Not OK \n")
            return False

        print("Graphite: OK \n")
        return True

    def kibana_status(self):
        print("Checking Kibana Status")
        url = 'http://localhost:9005'

        result = self.request_center(url)
        if result is False:
            print("Kibana: Not OK \n")
            return False
        print("Kibana: OK \n")
        return True

if __name__ == '__main__':
    import argparse
    import os

    choices = ['up', 'purge', 'status', 'docker', 'vagrant']
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('opertion', help='What Opertion you want to do.', choices=choices)
    parser.add_argument('--cmd', help='Adding command to Docker or Vagrant.')
    args = parser.parse_args()

    if args.opertion == 'status':
        s1, s2, s3, s4 = main().grafana_status(), main().prometheus_status(), \
                         main().graphite_status(), main().kibana_status()

        if s1 and s2 and s3 and s4:
            print("Stack is up and running.")
        else:
            sdic = {
                'grafana': s1,
                'prometheus': s2,
                'graphite': s3,
                'kibana': s4
            }
            for i in sdic:
                if not sdic[i]:
                    print("{} Not working properly".format(i))
    elif args.opertion == 'up':
        os.system('vagrant up')
    elif args.opertion == 'purge':
        os.system('vagrant destroy')
    elif args.opertion == 'vagrant':
        os.system('vagrant {}'.format(args.cmd))
    elif args.opertion == 'docker':
        os.system('vagrant ssh -c "docker {}"'.format(args.cmd))
