from flask_frozen import Freezer
from app import app  # app.py에서 생성한 Flask 객체(app)를 가져옵니다.

app.config['FREEZER_BASE_URL'] = 'https://sks3297.github.io/wedding-invitation/'
# Flask 3.x 버전과 Frozen-Flask 호환성 (url_adapter) 문제 해결을 위한 서버 설정
app.config['SERVER_NAME'] = 'sks3297.github.io'
app.config['APPLICATION_ROOT'] = '/wedding-invitation'

freezer = Freezer(app)

if __name__ == '__main__':
    # Flask 앱을 정적 파일(HTML)로 변환하여 'build' 폴더에 저장합니다.
    # __init__.py generator 내부의 test_request_context 유실 방지
    with app.app_context():
        with app.test_request_context(base_url=app.config['FREEZER_BASE_URL']):
            freezer.freeze()