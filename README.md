# ✅ 로컬 환경에서 실행 방법
- 편의를 위해 SQLite3를 사용합니다.

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
- Makefile에 정의된 명령어를 사용하여 서버를 실행합니다.

## URL 접속
👉 [서버 주소 (127.0.0.1:8000)](http://127.0.0.1:8000/)

---

# ✅ Docker Compose 실행 방법
- PostgreSQL을 DB로 사용합니다.
- 개발 시, 디스크 공간 부족으로 로컬 환경에 postgres_data 폴더를 생성합니다.

## Docker 컨테이너 실행 및 마이그레이션
```
make docker-build-and-migrate
```
- Makefile에 정의된 명령어를 사용하여 컨테이너를 실행합니다.

## Docker 컨테이너 제거 (컨테이너, 볼륨, postgres_data)
```
make docker-prune-all
```
- Makefile에 정의된 명령어를 사용하여 컨테이너를 제거합니다.

## URL 접속
👉 [서버 주소 (0.0.0.0:8000)](http://0.0.0.0:8000/)

## Swagger
👉 [http://0.0.0.0:8000/doc/](http://0.0.0.0:8000/doc/)

## 전체 상품
👉 [http://0.0.0.0:8000/shop/products/](http://0.0.0.0:8000/shop/products/)

## 개별 상품 (pk: 1)
👉 [http://0.0.0.0:8000/shop/products/1/](http://0.0.0.0:8000/shop/products/1/)

---

# ✅ 테스트 코드 실행하기

## 전체 테스트 실행
```
pytest shop/tests.py -v -s
```

## 특정 테스트 함수만 실행
```
pytest shop/tests.py::test_create_product -v -s
```

```
pytest shop/tests.py::test_patch_product -v -s
```

- `-v` 옵션을 통해 테스트 동작 과정을 자세히 확인할 수 있습니다.  
- `-s` 옵션을 통해 print된 응답 데이터를 확인할 수 있습니다.
- `Makefile`을 사용하지 않은 이유는 테스트 할 파일의 경로를 특정해줘야 하기