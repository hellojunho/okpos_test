# 로컬 환경에서 실행 방법
>  편의를 위해 SQLite3를 사용합니다.

## 가상환경 설정 및 requirements.txt 설치하기
```
python3.8 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

## DB 초기화 및 서버 실행하기
```
make reset-local-server
```

## URL 접속
👉 [서버 주소 (127.0.0.1:8000)](http://127.0.0.1:8000/)


# Docker Compose 실행 방법
> PostgreSQL을 DB로 사용합니다.
> 개발 시, 디스크 공간 부족으로 로컬 환경에 postgres_data 폴더를 생성합니다.

## Docker 컨테이너 실행하기
```
docker-compose up --build
```

## shell 접속하기
```
docker exec -it okpos_test-web-1 /bin/bash
```

## 마이그레이션 하기
```
python manage.py makemigrations

python manage.py migrate
```

## URL 접속
👉 [서버 주소 (0.0.0.0:8000)](http://0.0.0.0:8000/)
