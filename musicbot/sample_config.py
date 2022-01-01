class Config(object):
    token = '' # 봇 토큰
    EXTENSIONS = ['owners',
                'help',
                'owners',
                'music',
                'set_language',
                'chart']

    OWNERS = [123456789] # 관리자의 아이디
    commandInt = "" # 명령인자
    BOT_NAME = "" # 봇 이름
    BOT_TAG = "#" # 태그
    BOT_VER = "" # 버전
    BOT_ID = 123456789      # 봇 아이디
    AboutBot = "" # 봇 정보

    # Music
    host = "localhost"
    psw = "" # 컴퓨터 비밀번호
    region = "eu" # 리전
    port = 2333

    color_code = 0xc68e6e # 색상코드

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True
