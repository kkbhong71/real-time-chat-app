# 🎯 실시간 채팅 웹앱

바이브 코딩으로 만든 파이썬 Flask 기반 실시간 채팅 웹 애플리케이션입니다.

## ✨ 주요 기능

- 🚀 **실시간 메시지 송수신**: WebSocket을 통한 즉각적인 메시지 전달
- 👤 **간단한 닉네임 시스템**: 별도 회원가입 없이 닉네임만으로 참여
- 🎨 **반응형 디자인**: 모바일과 데스크톱 모두 지원
- 💬 **사용자 입장/퇴장 알림**: 실시간 사용자 상태 표시
- 🔄 **자동 재연결**: 네트워크 끊김 시 자동 복구 시도

## 🛠 기술 스택

- **Backend**: Python, Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript, Socket.IO
- **배포**: Render.com
- **버전 관리**: Git, GitHub

## 🚀 로컬 개발 환경 설정

### 1. 저장소 클론
```bash
git clone https://github.com/yourusername/real-time-chat-app.git
cd real-time-chat-app
```

### 2. 가상환경 생성 및 활성화
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```

웹 브라우저에서 `http://localhost:5000`에 접속하여 채팅 앱을 사용할 수 있습니다.

## 🌐 배포 방법 (Render.com)

### 1. GitHub 저장소 준비
- 프로젝트를 GitHub에 업로드
- `main` 브랜치에 모든 파일이 포함되어 있는지 확인

### 2. Render.com 설정
1. [Render.com](https://render.com)에 가입 및 로그인
2. "New +" 버튼 클릭 → "Web Service" 선택
3. GitHub 저장소 연결
4. 다음 설정 사용:
   - **Name**: 원하는 서비스 이름
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:$PORT app:app`

### 3. 환경 변수 설정 (선택사항)
- `SECRET_KEY`: Flask 세션 보안을 위한 비밀 키

## 📁 프로젝트 구조

```
real-time-chat-app/
│
├── app.py                 # 메인 Flask 애플리케이션
├── requirements.txt       # Python 의존성 패키지
├── Procfile              # Render.com 배포 설정
├── .gitignore            # Git 무시 파일
├── README.md             # 프로젝트 설명서
│
├── templates/            # HTML 템플릿
│   ├── index.html        # 메인 페이지 (닉네임 입력)
│   └── chat.html         # 채팅방 페이지
│
└── static/               # 정적 파일
    └── css/
        └── style.css     # 스타일시트
```

## 🔧 사용 방법

1. **웹사이트 접속**: 배포된 URL 또는 로컬 개발 서버에 접속
2. **닉네임 입력**: 2-20자의 닉네임을 입력하고 채팅방 입장
3. **메시지 전송**: 하단 입력창에 메시지를 입력하고 Enter 키 또는 전송 버튼 클릭
4. **실시간 채팅**: 다른 사용자들과 실시간으로 메시지 주고받기

## ⚠️ 주의사항 (무료 호스팅)

- **콜드 스타트**: 첫 접속 시 5-10초의 로딩 시간이 있을 수 있습니다
- **슬립 모드**: 15분간 비활성 시 서버가 슬립 모드로 전환됩니다
- **동시 접속자**: 무료 플랜은 동시 접속자 수에 제한이 있을 수 있습니다

## 🔮 향후 개선 계획

- [ ] 다중 채팅방 지원
- [ ] 사용자 인증 시스템
- [ ] 메시지 히스토리 저장
- [ ] 파일 업로드 기능
- [ ] 이모지 지원
- [ ] 음성/화상 채팅

## 🤝 기여하기

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자유롭게 사용, 수정, 배포할 수 있습니다.

## 👨‍💻 개발자

**바이브 코딩 학습자**
- 실시간 웹 애플리케이션 개발 연습 프로젝트
- Flask와 Socket.IO를 활용한 첫 번째 실시간 앱

---

**🎉 즐거운 채팅하세요! 🎉**
