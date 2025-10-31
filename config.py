import os

class Config(object):
####Dynamic Configs Variables####
    BOT_TOKEN = os.environ.get("7590266354:AAEGaPWU_uV2JErJ_HrBwTnL06LiQ4p0Itw")
    DB_NAME = os.environ.get("uploaderbot")
####Static Configs Variables####
    API_ID = 22484497 #API ID
    API_HASH = "c38cb053916c47a97590c244663cbaef" #API HASH
    ADMIN_ID = 6252997817 #Admin ID
    DB_URL = "mongodb+srv://uploaderbot:uploaderbot@cluster0.mpesxpw.mongodb.net/?retryWrites=true&w=majority" #Database URL
    TXT_LOG = -1003171881798 #Text Log Channel ID
    LOG_CHANNEL = -1003171881798 #Log Channel ID
    CREDIT = "Unknown" #Credit
    PROXY = "103.172.85.194:50100" #Socks5 Proxy

