# ElasticSearch
## 자원
||CPU|MEM|Program|
|:--:|--:|--:|--:|
|우분투|2|4|ElasticSearch, Kibana|
|우분투|2|1|Logstash|

## Installation
```shell
apt  update
apt  install  -y  openjdk-8-jdk

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
apt update
apt install elasticsearch
```
## yaml

```shell
/etc/elasticsearch/elasticsearch.yml
```
```
network.host: 0.0.0.0		<- 엘라스틱이 설치된 컴퓨터의 IP
discovery.seed_hosts: ["ES_host"]	<- 엘라스틱이 설치된 컴퓨터의 IP
```


## Exec
```shell
curl -XGET localhost:9200
systemctl status elasticsearch
# 키는법
systemctl start elasticsearch
```
