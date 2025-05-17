import os

class Config(object):
####Dynamic Configs Variables####
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DB_NAME = os.environ.get("DB_NAME")
####Static Configs Variables####
    API_ID = 7359282 #API ID
    API_HASH = "" #API HASH
    ADMIN_ID = 739279231 #Admin ID
    DB_URL = "" #Database URL
    TXT_LOG = -100 #Text Log Channel ID
    LOG_CHANNEL = -100 #Log Channel ID
    CREDIT = "Unknown" #Credit
    PROXY = "103.172.85.194:50100" #Socks5 Proxy
