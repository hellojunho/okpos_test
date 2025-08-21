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

## .env ENVIRONMENT 변수 값 설정하기
```
ENVIRONMENT="local"
```
- 제출 시 기본 값으로는 `"docker"`로 설정했습니다.

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

## .env ENVIRONMENT 변수 값 설정하기
```
ENVIRONMENT="docker"
```

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

## Docker 컨테이너 안에서의 명령어
```
docker exec -it okpos_test-web-1 /bin/bash
```
- 위 명령어를 입력하면 django 컨테이너에 접속하여 명령어를 입력할 수 있습니다.

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
pytest shop/tests/* -v -s
```

## 특정 테스트 함수만 실행
```
pytest shop/tests/test_create_product.py -v -s
```

```
pytest shop/tests/test_patch_product.py -v -s
```

- `-v` 옵션을 통해 테스트 동작 과정을 자세히 확인할 수 있습니다.  
- `-s` 옵션을 통해 print된 응답 데이터를 확인할 수 있습니다.

## 테스트 결과 예시 화면

### test_create_product.py
<img width="836" height="745" alt="Image" src="https://github.com/user-attachments/assets/82995e8b-6805-4f59-bdf7-99011182d87d" />

### test_patch_product.py
<img width="835" height="783" alt="Image" src="https://github.com/user-attachments/assets/41c9d139-10b5-404e-8ef5-d77136cacf61" />

---

# Github Action
- `main` 브랜치로 Push를 하게되면 [Actions](https://github.com/hellojunho/okpos_test/actions) 에서 Github Action의 동작을 확인할 수 있습니다.
- docker compose를 사용하여 컨테이너를 올리고, 그 안에서 `pytest`를 실행합니다.

## 결과 예시 화면
<img width="584" height="614" alt="Image" src="https://github.com/user-attachments/assets/e92e1845-cc1f-4477-83e7-344de06c3c94" />

# CodeCov 결과 예시 화면
<img width="837" height="643" alt="Image" src="https://github.com/user-attachments/assets/37ae9ccb-da54-466d-98fa-c7c019c93836" />
