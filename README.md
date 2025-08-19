# 실행 방법
### 1. 가상환경
```
python3.8 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

### 2. Docker-Compose 실행하기
```
docker-compose up --build
```

### 3. Docker-Compose 중지하기
```
docker-compose down
```


### 4. (로컬) 서버 초기화 및 실행하기
```
make reset-local-server
```

### 5. (로컬) 서버 실행하기
```
python manage.py runserver
```

### 테스트 코드 실행 방법







# TODO
- PEP8 -> pro-commit
- python3.8, django2.2.24
    ```
    python3.8 -m venv venv
    source venv/bin/activate
    pip install "Django==2.2.24"
    ```
- requirements.txt
    ```
    pip freeze > requirements.txt
    ```
- django 실행 방법
- Postman Export 결과 첨부
- API Test 코드 작성
- `drf-writable-nested` 사용
- `ModelViewSet` 사용
- Django ORM 최적화 한 쿼리 사용
- `Dockerfile`, `docker-compose` 사용
- `Docker` 사용 방법 README
- `swagger` 사용 및 `/doc/` 로 경로 설정
- `pytest` 권장 및 README
- 커버리지 측정 (`codecov` 권장)
- `Github Action`을 사용한 테스트 자동화 및 커버리지 결과 전송# okpos_project
