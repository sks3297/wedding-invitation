from flask_frozen import Freezer
from app import app  # app.py에서 생성한 Flask 객체(app)를 가져옵니다.

app.config['FREEZER_BASE_URL'] = 'https://sks3297.github.io/wedding-invitation/'

freezer = Freezer(app)

if __name__ == '__main__':
    # Flask 앱을 정적 파일(HTML)로 변환하여 'build' 폴더에 저장합니다.
    freezer.freeze()