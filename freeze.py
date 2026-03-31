import os
import shutil
from app import app, index

if __name__ == '__main__':
    # 1. 빌드 폴더 준비 및 초기화
    build_dir = os.path.join(os.path.dirname(__file__), 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)
    
    # 2. Flask 3.x의 Frozen-Flask 호환성 에러 우회하기 위한 수동 렌더링 방식
    # (단일 페이지 웨딩 청첩장에 가장 안정적인 해결책)
    with app.app_context():
        with app.test_request_context('/', base_url='https://sks3297.github.io/wedding-invitation/'):
            # 실제 홈페이지 함수를 실행시켜 HTML 결과물을 받아옴
            html_content = index()
            
            # GitHub Pages 등 정적 호스팅 사이트에서 상대 경로로 정상 동작하도록 변환
            html_content = html_content.replace('"/static/', '"static/')
            html_content = html_content.replace("'\/static/", "'static/")
            
            with open(os.path.join(build_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html_content)
                
    # 3. CSS, 이미지, BGM 등 정적(Static) 파일 원본 복사
    static_src = os.path.join(os.path.dirname(__file__), 'static')
    static_dest = os.path.join(build_dir, 'static')
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dest)
        
    print("정적 파일 빌드가 완료되었습니다. (build 폴더 렌더링 완료)")