# Logstash
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
apt install logstash
```
## conf

```shell
vi /etc/logstash/conf.d/logstash.conf
```
```
input {
  tcp {
    port => 5000
    codec => json { charset => "UTF-8" }
  }
}

filter {
  mutate {
    remove_field => [ "port", "path", "message", "@version", "@timestamp", "host" ]
  }
}

output {
  elasticsearch {
    hosts => ["http://192.168.216.135:9200"]
    index => "coffee"
  }
}
```


## Exec
```shell
curl -XGET localhost:9200
systemctl status elasticsearch
# 키는법
systemctl start elasticsearch
```
