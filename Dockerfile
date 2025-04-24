# 베이스 이미지 설정 (Python 3.9 사용)
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 현재 폴더의 모든 파일을 Docker 컨테이너의 /app 폴더로 복사
COPY . /app

# 필요한 라이브러리 설치 (requirements.txt 파일 사용)
RUN pip install --no-cache-dir -r requirements.txt

# 포트 설정 (로컬에서 접속하기 위해 필요)
EXPOSE 8000

# 컨테이너 실행 시 실행될 명령어 (app.py 실행)
CMD ["python", "app.py"]