# OpenWebUI_trial

웹 기반 사용자 인터페이스 애플리케이션 open web ui 테스트 입니다.

## 프로젝트 개요

이 프로젝트는 웹 기반 사용자 인터페이스를 제공하는 애플리케이션입니다. Docker를 통한 컨테이너화가 지원되며, Python 기반으로 개발되었습니다.

## 주요 기능

- 웹 기반 사용자 인터페이스
- Docker 컨테이너 지원
- 대화형 인터페이스

## 설치 방법

### 필수 요구사항

- Python 3.x
- Docker (선택사항)

### 로컬 환경에서 실행하기

1. 저장소 클론:

```bash
git clone [저장소 URL]
cd openwebui
```

2. 가상환경 생성 및 활성화:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치:

```bash
pip install -r requirements.txt
```

4. 애플리케이션 실행:

```bash
python app.py
```

### Docker를 사용하여 실행하기

1. Docker 이미지 빌드:

```bash
docker build -t openwebui .
```

2. Docker 컨테이너 실행:

```bash
docker run -p 5000:5000 openwebui
```

## 프로젝트 구조

```
openwebui/
├── app.py              # 메인 애플리케이션 파일
├── Dockerfile          # Docker 설정 파일
├── requirements.txt    # Python 의존성 목록
├── cleanup.sh          # 정리 스크립트
└── conversations/      # 대화 데이터 디렉토리
```

## 사용 방법

애플리케이션 실행 후 웹 브라우저에서 `http://localhost:8000`으로 접속하여 사용할 수 있습니다.

## 기여하기

1. 이 저장소를 포크합니다.
2. 새로운 기능 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
