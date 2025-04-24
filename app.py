import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 설정을 위한 라이브러리
import os

app = Flask(__name__)
CORS(app)  # 모든 도메인에서 접근 허용

# 대화 로그 저장 경로 설정
LOG_FILE = "./conversations/conversation_log.json"

# 대화 저장 폴더가 없다면 생성
if not os.path.exists("./conversations"):
    os.makedirs("./conversations")

# 간단한 모델 응답 함수 (테스트용)
def generate_response(user_input):
    return f"사용자가 입력한 내용: {user_input}"  # 여기에 모델 응답을 생성하는 코드를 넣어야 함

@app.route("/", methods=["GET"])
def home():
    return "Open Web UI 서버가 성공적으로 실행되었습니다. 대화하려면 '/chat' 엔드포인트로 POST 요청을 보내세요."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("user_input")
        
        if not user_input:
            return jsonify({"error": "user_input 값이 제공되지 않았습니다."}), 400
        
        # 모델 응답 생성
        model_output = generate_response(user_input)

        # 대화 로그 저장하기
        save_conversation(user_input, model_output)
        
        return jsonify({"model_output": model_output})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def save_conversation(user_input, model_output):
    data = {
        "timestamp": str(datetime.now()),
        "user_input": user_input,
        "model_output": model_output
    }
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)