# Starbucks_Ediya 매장간 거리 관계 분석<br>

## 0. 들어가기전
![image](https://user-images.githubusercontent.com/81276472/157696015-a293c60f-2f02-43dc-92e3-e1c3783a852e.png)
- 출처 : http://www.iconsumer.or.kr/news/articleView.html?idxno=10133
- '스타벅스 옆에는 이디야가 있다.', '파리바게뜨는 대부분 매장이 아파트 단지 입구나 횡단보도 앞에 있고, 그 주위에는 분식 프랜차이즈 '아딸'이 자리한다.', '설빙은 2층에 있다' 등 이러한 이야기를 들어본적이 있을 것이다. 우리는 진위여부를 알아보기 위해 ELK를 사용해 수집, 처리, 저장, 분석, 시각화를 해볼 예정이다.<br><br><br>

## 1. 개발환경 및 사용기술
### 1) 개발환경
- PyCham Community
- GitHub
- Linux
<br><br>
### 2) 사용기술
- Python(3.9)
- Ubuntu(18.04)
- ElasticSearch
- Logstash
- Kibana
<br><br>

## 2. 구현 기능
- Map
- Metric
- Pie Chart
- Vertical Chart
<br><br>

## 3. 시스템 흐름도
![image](https://user-images.githubusercontent.com/81276472/157697558-ec270d52-b00e-4612-a85e-2049474e94a4.png)
<br><br>

## 4. 결과
### 1) 서울 총 매장 수
![image](https://user-images.githubusercontent.com/81276472/157687196-66de576b-e192-4878-ac35-abca8c2295c7.png)
- 2021.12.31기준 서울의 스타벅스와 이디야의 총 매장 수는 871개로 확인됨
<br><br>

### 2) 각 매장 점유율
![image](https://user-images.githubusercontent.com/81276472/157687632-45da5962-48e2-4fdd-b447-0708f1a1e068.png)
- 서울의 매장 점유율은 스타벅스가 약 7.7%로 더 많은 모습을 볼 수 있었음
<br><br>

### 3) 시군구별 매장 수 Top 10
![image](https://user-images.githubusercontent.com/81276472/157690856-955f01c0-0574-4ba1-a824-483f9dcbc176.png)
- 서울에서 강남구가 커피 매장 수가 가장 많은 모습을 확인할 수 있었음
- 스타벅스는 상권이 크게 발달하거나 유동인구가 많은 강남구 주변으로 가게가 많은 모습을 확인할 수 있음
- 이디야는 강서구에서 크게 점유율를 가지는 모습이 확인됨 > 상권이 강남과 비교했을 때, 작고 매장을 크게 짓는 스타벅스보다 작은 매장도 있는 이디야 커피점이 많은 모습을 볼 수 있었음
<br><br>

### 4) 스타벅스 및 이디야 위치 정보
![image](https://user-images.githubusercontent.com/81276472/157695038-3fe2a691-0be5-4806-8db5-61f0d71cb881.png)
- 스타벅스 및 이디야가 100m 이내에 붙어있던 매장은 총 94개였음

## 5. 후기
![image](https://user-images.githubusercontent.com/81276472/157688051-c4859bed-330e-44c8-9a6f-228e95e03d9c.png)
- 앞서 스타벅스를 따라다녔다는 이디야 기사에 비해 생각보다 근처에 커피가 붙어있다는 느낌을 받지 못했다. 처음에는 50m를 기준으로 했을 때에는 약 60개의 지점이 붙어있을 정도로 매우 적었다.

- 코드에서는 871개의 데이터가 서로의 관계를 알기위해 n*n번의 계산을 거친다. 이는 데이터가 커지면 커질수록 무겁고 비효율적인 코드가 될 가능성이 높다. 따라서, 수정이 필요함.
