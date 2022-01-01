import os
import sys
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)
ENV = bool(os.environ.get('ENV', False))
if ENV:
    token            = os.environ.get('token', None)
    try:
        EXTENSIONS   = set(str(x) for x in os.environ.get("EXTENSIONS", 'owners help other ping about music melon').split())
    except ValueError:
        raise Exception("모듈 목록이 올바르지 않습니다.")
    try:
        OWNERS       = set(int(x) for x in os.environ.get("OWNERS", "").split())
    except ValueError:
        raise Exception("OWNERS 사용자 목록에 올바른 정수가 없습니다.")
    commandInt       = os.environ.get('commandInt', "/")
    BOT_NAME         = os.environ.get('BOT_NAME', None)
    BOT_TAG          = os.environ.get('BOT_TAG', "#1234")
    BOT_VER          = os.environ.get('BOT_VER', None)
    try:
        BOT_ID       = int(os.environ.get('BOT_ID', None))
    except ValueError:
        raise Exception("BOT_ID에 올바른 정수가 없습니다.")
    color_code       = int(os.environ.get('color_code', "0xc68e6e"), 0)
    AboutBot         = os.environ.get('AboutBot', None)
    host             = os.environ.get('host', "localhost")
    psw              = os.environ.get('psw', None)
    region           = os.environ.get('region', "en")
    port             = int(os.environ.get('port', 2333))

else:
    from musicbot.config import Development as Config

    token           = Config.token
    EXTENSIONS       = Config.EXTENSIONS
    OWNERS           = Config.OWNERS
    commandInt       = Config.commandInt
    BOT_NAME         = Config.BOT_NAME
    BOT_TAG          = Config.BOT_TAG
    BOT_VER          = Config.BOT_VER
    BOT_ID           = Config.BOT_ID
    color_code       = Config.color_code
    AboutBot         = Config.AboutBot
    host             = Config.host
    psw              = Config.psw
    region           = Config.region
    port             = Config.port

EXTENSIONS = list(EXTENSIONS)
BOT_NAME_TAG_VER = "%s%s | %s" %(BOT_NAME, BOT_TAG, BOT_VER)
f = open("application.yml", 'w')
f.write(f"""server:
  port: {port}
  address: {host}
spring:
  main:
    banner-mode: log
lavalink:
  server:
    password: "{psw}"
    sources:
      youtube: true
      bandcamp: true
      soundcloud: true
      twitch: true
      vimeo: true
      mixer: true
      http: true
      local: false
    bufferDurationMs: 400
    youtubePlaylistLoadLimit: 6
    playerUpdateInterval: 5
    youtubeSearchEnabled: true
    soundcloudSearchEnabled: true
    gc-warnings: true

metrics:
  prometheus:
    enabled: false
    endpoint: /metrics

sentry:
  dsn: ""
  environment: ""

logging:
  file:
    max-history: 30
    max-size: 1GB
  path: ./logs/

  level:
    root: INFO
    lavalink: INFO""")
f.close()
