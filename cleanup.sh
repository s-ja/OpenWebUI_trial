#!/bin/bash

# Docker 컨테이너와 이미지 정리 스크립트
echo "Docker 컨테이너와 이미지 정리 시작..."

# 실행 중인 컨테이너 중지
echo "실행 중인 컨테이너 중지 중..."
docker stop $(docker ps -q) 2>/dev/null || true

# 모든 컨테이너 삭제
echo "모든 컨테이너 삭제 중..."
docker rm $(docker ps -a -q) 2>/dev/null || true

# 이미지 삭제
echo "openwebui 이미지 삭제 중..."
docker rmi openwebui 2>/dev/null || true

echo "정리 완료!" 