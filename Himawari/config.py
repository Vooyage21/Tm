"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and
# import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/Himawari/{config}", "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # dont change
    LOGGER = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    LOAD = ""
    NO_LOAD = ""  # put some module name here if you do not want it to load
    MONGO_DB = "Helmi4636"
    BOT_API_URL = "https://api.telegram.org/bot"

    # you can change these
    DEL_CMDS = False  # set it to true if you want the "/" commands to be deleted
    INFOPIC = True  # picture while doing /info
    STRICT_GBAN = True  # IF YOU WANT TO ENABLE GBAN SYSTEM
    API_ID =  # api id from my.telegram.org
    API_HASH = ""  # api hash from my.telegram.org
    # mongo database link (necessary)
    MONGO_DB_URL = "mongodb+srv://Xyxx:Helmi4636@cluster0.9yy5ve9.mongodb.net/?retryWrites=true&w=majority"
    DB_URL = "postgres://thpyouro:Xt9VN1Ybhm9bs8SBk-DU6Jwd6nt_BuGn@bubble.db.elephantsql.com/thpyouro"  # postgres sql database link
    # redis database url from redislabs.com
    REDIS_URL = "http://redis-19497.c281.us-east-1-2.ec2.cloud.redislabs.com:19497"
    TOKEN = "54dssdV8e59Odo"  # bot token from @BotFather
    DEV_USERS = [940232666]  # developers id
    SUDO_USERS = [940232666]  # sudo users id
    SUPPORT_USERS = [940232666]  # support user ids
    WHITELIST_USERS = [940232666]  # commas for multiple ids
    EVENT_LOGS =   # channel id for gban logs
    OWNER_ID = 940232666  # owner id in integer
    ERROR_LOGS =  # support group id
    BOT_NAME = "Mizu Robot"  # your bot name
    ARQ_API_KEY = "SLSFXSsdUXNSMH-ARQ"  # ARQ api key from @ARQRobot
    ARQ_API_URL = "http://thearq.tech/"  # arq link
    SUPPORT_CHAT = "Ignidsn"  # support group username without @
    UPDATES_CHANNEL = "Igsd"  # Updates/News Channel username without @
    BOT_USERNAME = ""  # bot username without @
    REM_BG_API_KEY = "K2dsdsYma6cZx"  # not necessary


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
