from flask import Flask, render_template
import datetime

app = Flask(__name__)

# ==========================================
# [설정] 여기만 수정하면 내용이 바뀝니다.
# ==========================================

# 1. 카카오맵 API 키 (카카오 개발자 센터에서 발급 필요)
# KAKAO_MAP_API_KEY = '2944d204a72efd86b8d0d2ed7fe5bea3' # 프롬투데이 느낌을 위해 키는 꼭 넣어주세요!
KAKAO_MAP_API_KEY = 'REPLACE_KAKAO_MAP_API_KEY' # 프롬투데이 느낌을 위해 키는 꼭 넣어주세요!

# 2. 예식장 좌표 (구글맵이나 카카오맵에서 확인한 위도, 경도)
WEDDING_LAT = 37.508628
WEDDING_LNG = 126.888733
WEDDING_HALL_NAME = '더 세인트'
WEDDING_ADDRESS = '서울특별시 구로구 경인로 662 디큐브시티 6층-그랜드볼룸'
WEDDING_DATE_OBJ = datetime.date(2026, 5, 2)

GALLERY_IMAGE_COUNT = 7

GROOM_GIVEN_NAME = '{GROOM_GIVEN_NAME}'
BRIDE_GIVEN_NAME = '{BRIDE_GIVEN_NAME}'

@app.route('/')
def index():
    today = datetime.date.today()
    d_day_delta = WEDDING_DATE_OBJ - today
    d_day_text = f'{GROOM_GIVEN_NAME} & {BRIDE_GIVEN_NAME}의 결혼식이 {d_day_delta.days}일 남았습니다.' if d_day_delta.days >= 0 else f'결혼했습니다 (+{abs(d_day_delta.days)})'

    invitation_data = {
        'wedding_date': '2026년 5월 2일 토요일 오전 11시 30분',
        'wedding_hall': WEDDING_HALL_NAME,
        'address': WEDDING_ADDRESS,
        
        'groom_name': '{GROOM_NAME}',
        'groom_account': '{GROOM_ACCOUNT}',
        'groom_account_bank': '{GROOM_ACCOUNT_BANK}',
        'groom_phone': '{GROOM_PHONE}',

        'bride_name': '{BRIDE_NAME}',
        'bride_account': '{BRIDE_ACCOUNT}',
        'bride_account_bank': '{BRIDE_ACCOUNT_BANK}',
        'bride_phone': '{BRIDGE_PHONE}',

        'groom_parent_account_bank': '{GROOM_PARENT_ACCOUNT_BANK}',
        'groom_parent_account_name': '{GROOM_PARENT_ACCOUNT_NAME}',
        'groom_parent_account': '{GROOM_PARENT_ACCOUNT}',

        'bride_parent_account_bank': '{BRIDE_PARENT_ACCOUNT_BANK}',
        'bride_parent_account_name': '{BRIDE_PARENT_ACCOUNT_NAME}',        
        'bride_parent_account': '{BRIDE_PARENT_ACCOUNT}',
        
        # 지도 설정을 함께 전달
        'map_api_key': KAKAO_MAP_API_KEY,
        'lat': WEDDING_LAT,
        'lng': WEDDING_LNG,
        'd_day': d_day_text,
        # 'wedding_date_ymd': WEDDING_DATE_OBJ.strftime('%Y.%m.%d'), # 달력용 YYYY.MM.DD
        'calendar_month': WEDDING_DATE_OBJ.strftime('%b').upper(),
        'calendar_day': WEDDING_DATE_OBJ.strftime('%d'),

        'gallery_count': GALLERY_IMAGE_COUNT
    }
    
    return render_template('index.html', data=invitation_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)