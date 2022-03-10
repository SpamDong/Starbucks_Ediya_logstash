import json
import logging
from logging import StreamHandler
import logstash
from haversine import haversine


host = '192.168.66.136'

test_logger = logging.getLogger('python-logstash-logger')

test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))
test_logger.addHandler(StreamHandler())

inout_f = open("seoul.csv", 'r', encoding="UTF-8")
inout_lines = inout_f.readlines()

json_f = open("coffee.json", 'w', encoding="UTF-8")

store_type = []
store_name = []
store_type = []
store_addr = []
store_city = []
store_gu = []
store_dong = []
lat = []
lon = []
store_result = []

for idx in range(1, len(inout_lines)):
    inout_line = inout_lines[idx]

    name = inout_line.split(',')[1].replace("\"", "") # 가게 이름

    if '스타벅스' in name:
        store_type.append("Starbucks")

    elif '이디야커피' in name:
        store_type.append("Ediya")
    else:
        continue
    store_name.append(inout_line.split(',')[1].replace("\"", "")) # 가게 이름
    lon.append(float(inout_line.split(',')[-2]))# 경도
    lat.append(float(inout_line.split(',')[-1].replace("\n", "")))# 위도
    store_addr.append(inout_line.split(',')[24].replace("\"", ""))# 가게 지번
    store_city.append(inout_line.split(',')[12].replace("\"", ""))# 서울특별시
    store_gu.append(inout_line.split(',')[14].replace("\"", ""))# OO구
    store_dong.append(inout_line.split(',')[16].replace("\"", ""))# OO동

for i in range(0,len(store_name)):
    store_result.append(False)

for i in range(0,len(store_name)):
    if '스타벅스' in store_name[i]:
        for j in range(0,len(store_name)):
            if '이디야' in store_name[j]:
                lyon = (lat[i],lon[i])  # (latitude, longtitude)
                paris = (lat[j],lon[j])
                # 거리 계산
                result = haversine(lyon, paris, unit='m')
                print(lat[i], lon[i])
                print(result)
                if result < 100:
                    store_result[i] = True
                    break

    elif '이디야' in store_name[i]:
        for j in range(0,len(store_name)):
            if '스타벅스' in store_name[j]:
                lyon = (lat[i],lon[i])  # (latitude, longtitude)
                paris = (lat[j],lon[j])
                # 거리 계산
                result = haversine(lyon, paris, unit='m')
                print(lat[i], lon[i])
                print(result)
                if result < 100:
                    store_result[i] = True
                    break

print(store_result)

for i in range(0, len(store_name)):
    data = {
        "store_name": store_name[i],
        "store_type": store_type[i],
        "store_addr": store_addr[i],
        "store_city": store_city[i],
        "store_gu": store_gu[i],
        "store_dong": store_dong[i],
        "store_geo": {"lat": lat[i], "lon": lon[i]},
        "store_result": store_result[i],
    }
    json_f.write(json.dumps(data, ensure_ascii=False) + "\n")
    test_logger.info('Coffee2', extra=data)



inout_f.close()
json_f.close()