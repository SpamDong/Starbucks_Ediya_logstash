# Kibana
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
apt install kibana
```
## yaml

```shell
/etc/kibana/kibana.yml
```
```
elasticsearch.hosts: ["http://ES_host:9200"] <- 엘라스틱이 설치된 컴퓨터의 IP
```


## Exec
```shell
curl -XGET localhost:5601
systemctl status kibana
# 키는법
systemctl start kibana
```
- 웹브라우저로 > http://kibana_host:5601
