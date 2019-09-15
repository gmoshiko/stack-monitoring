# Jenkins
![alt text][logo]

[logo]: hellmo-300x300.png "HelmO"

-------
Jenkins is responsible for the interaction between the user and HelmO & CI/CD.  
Each HelmO repository have a Jenkins build under the name: ``helmo-reponame``.  
in this page, you can find explanations and demonstration of everything related to Jenkins with HelmO.


# Table of contents
* [DSL](#dsl)
* [Options](#options)
    * [project](#project)
    * [leader](#leader)
    * [operation](#operation)
    * [version](#version)
    * [dryrun](#dryrun)
    * [wait](#wait)
    * [present](#present)
    * [clusters](#version)
    * [safe](#safe)
    * [interactive](#interactive)
    * [helmocky](#helmocky)
    * [render](#render)
    * [confirm](#confirm)
* [Summary](#summary)
* [Pullscm](#pullscm)
* [Deployed](#deployed)
    

## DSL <a name="dsl"></a>
![Jenkins dsl!](dsl.png "Jenkins dsl")
  
## Options <a name="options"></a>
### Project 
project in HelmO is a Helm chart with  ``helmo_context.yml``.
Example HelmO project tree:

```bash
├── Chart.yaml
├── Makefile
├── README.md
├── helmo_context.yml
├── templates
│   ├── _helpers.tpl
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── tests
│   └── kibana_test.py
├── values
│   └── tlv
│       ├── values-tlv-ci.yaml
│       ├── values-tlv-infra.yaml
│       ├── values-tlv-qa.yaml
│       └── values-tlv-staticci.yaml
└── values.yaml

4 directories, 15 files
```
This is Kibana chart example, with the ``helmo_context.yml`` file giving HelmO context about the chart and LivePerson k8s infrastructure.  
more about "helmo_context.yml" in [contexts.md](contexts.md)

### Leader <a name="leader"></a>
leader is used for future developments.

### Operation <a name="operation"></a>
<b>Default: status</b>  
* [install](https://helm.sh/docs/helm/#helm-install)
* [upgrade](https://helm.sh/docs/helm/#helm-upgrade)
* [delete](https://helm.sh/docs/helm/#helm-delete)
* [status](https://helm.sh/docs/helm/#helm-status)
* [rollback](https://helm.sh/docs/helm/#helm-rollback)
  
### Version <a name="version"></a>
<b>Default: latest</b>  
Choose version received from harbor chart repository.  
more info about versions and CI in [repos.md](repos.md)

### Dryrun <a name="dryrun"></a>
<b>Default: true</b>  
Dryrun is recommended in any build, except in operation status.  
HelmO will run in dry-run mode first on all clusters, only if all dry-run return ok it will show the result in the console and wait for the user response if the build should continue.
dry-run is very important to HelmO as this is a good mechanism to check if HelmO can reach all the tillers you intended to. 

### Wait <a name="wait"></a>
<b>Default: true</b>  
If set, will wait until all Pods, PVCs, Services, and minimum number   
of Pods of a Deployment are in a ready state before marking the release as  
successful. It will wait for 10 minuts.

### Present <a name="present"></a>
<b>Default: labels</b>  
This parameter effects the [clusters](#clusters) options  
- ``contexts``: choose which clusters in format of "datacenter:k8s-cluster"
- ``labels``: choose from defaults labels & project labels  

For more information about labels & contexts please read [contexts.md](contexts.md)

### Clusters <a name="clusters"></a>
Clusters that are in ``helmo_contexts.yml`` of the choosed [project](#project),
for more information about clusters read [contexts.md](contexts.md)

### Safe <a name="safe"></a>
<b>Default: true</b>  
it can be used only if 2 or more clusters been chosen and not operation status.  
if set, will run on the first cluster and wait for user input when to continue,  
its recommenced to use it and manually check if everything went as expected. 

### Interactive <a name="interactive"></a>
<b>Default: true</b>  
**EXPERIMENTAL**  
if set, HelmO will not abort immediately if it got a failure.  
instead, it will try to recover and ask for user input what should be done next.  
Options: 
- ``retry``: retry again on the failed cluster and continue if pass.
- ``continue``: pass the failed cluster and continue with the rest of the clusters.
- ``abort``: abort the build.

### Helmocky <a name="helmocky"></a>
<b>Default: False</b>  
**DEVELOPMENT**  
if set, HelmO will use mock helm binary, so you can test any feature on this list without worrying to destroy anything. 
this is open only for the POC stage.  
after the POC is over this option will be removed from Jenkins.

### Render <a name="render"></a>
<b>Default: false</b>  
Will render [summary](#summary) from user selected parameters
 
### Confirm <a name="confirm"></a>
<b>Default: false</b>  
Only if the user confirms the summary the build can start, else the build will fail.
[summary](#summary) will change color and add confirmed verification 

## Summary <a name="summary"></a>
![Summary](summary.png "Summary")
HTML summary page.  
when the summary background in red, the build cannot be started, if it's green and you see your username  verification you can press the "Build" button.

## Pullscm <a name="pullscm"></a>
Each chart version is saved on Harbor project chart repository.
Jenkins will check every minute if there is a change in HelmO project Github repo. 
if there is change, will pull and update local HelmO project repo, if the chart version inside  
"Chart.yaml" file was raised compared to the latest version in project Harbor repository, HelmO will package and push the new image to Harbor.
more information on [repos.md](repos.md)

## Deployment <a name="deployment"></a>
HelmO will deploy the chart under the name: ``helmo_reponame_chartname``, the reason the name has to change and to have context to HelmO and the repository is to prevent abusing and mistaking, that way HelmO can be used and operation only on managed charts by HelmO, without mixing multiple repositories. 
