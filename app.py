from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
from datetime import datetime

# Flask 앱 초기화
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# SocketIO 초기화 (CORS 허용으로 다양한 도메인에서 접근 가능)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# 현재 접속한 사용자들을 저장할 딕셔너리
active_users = {}

@app.route('/')
def index():
    """메인 페이지 - 닉네임 입력 화면"""
    return render_template('index.html')

@app.route('/chat')
def chat():
    """채팅방 페이지"""
    nickname = request.args.get('nickname')
    if not nickname:
        # 닉네임이 없으면 메인 페이지로 리다이렉트
        return redirect(url_for('index'))
    return render_template('chat.html', nickname=nickname)

# Socket.IO 이벤트 핸들러들

@socketio.on('connect')
def handle_connect():
    """클라이언트가 연결될 때"""
    print(f'클라이언트 연결됨: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    """클라이언트가 연결 해제될 때"""
    print(f'클라이언트 연결 해제됨: {request.sid}')
    
    # 활성 사용자 목록에서 제거
    if request.sid in active_users:
        nickname = active_users[request.sid]['nickname']
        del active_users[request.sid]
        
        # 다른 사용자들에게 퇴장 알림
        emit('user_left', {
            'nickname': nickname,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, broadcast=True)

@socketio.on('join_chat')
def handle_join_chat(data):
    """사용자가 채팅방에 입장할 때"""
    nickname = data['nickname']
    
    # 활성 사용자 목록에 추가
    active_users[request.sid] = {
        'nickname': nickname,
        'joined_at': datetime.now()
    }
    
    # 채팅방에 입장
    join_room('main_chat')
    
    # 다른 사용자들에게 입장 알림
    emit('user_joined', {
        'nickname': nickname,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room='main_chat', include_self=False)
    
    # 본인에게는 환영 메시지
    emit('welcome_message', {
        'message': f'{nickname}님, 채팅방에 오신 것을 환영합니다!',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })

@socketio.on('send_message')
def handle_send_message(data):
    """메시지 전송 처리"""
    if request.sid not in active_users:
        return  # 등록되지 않은 사용자는 메시지 전송 불가
    
    nickname = active_users[request.sid]['nickname']
    message = data['message']
    timestamp = datetime.now().strftime('%H:%M:%S')
    
    # 모든 사용자에게 메시지 브로드캐스트
    emit('receive_message', {
        'nickname': nickname,
        'message': message,
        'timestamp': timestamp,
        'is_own': False  # 다른 사용자들에게는 자신의 메시지가 아님을 표시
    }, room='main_chat', include_self=False)
    
    # 보낸 사람에게는 자신의 메시지임을 표시
    emit('receive_message', {
        'nickname': nickname,
        'message': message,
        'timestamp': timestamp,
        'is_own': True
    })

# 에러 핸들러
@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return "서버 내부 오류가 발생했습니다.", 500

if __name__ == '__main__':
    # 개발 서버 실행 (Render.com에서는 gunicorn을 사용)
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
