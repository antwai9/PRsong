import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "bar_lo0o0")
ALIVE_NAME = getenv("ALIVE_NAME", "BARLO")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bar_lo0o0o0o0o")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "bar_lo0o0o0o0o")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/30452a15a60e0f95c5688.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/jankarikiduniya/Dr-Music-Video-Streaming")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/30452a15a60e0f95c5688.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/7261fcc96ecedd66dd126.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/30452a15a60e0f95c5688.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/7261fcc96ecedd66dd126.jpg")

# Don't Change It Bro ❣️ 😂


MY_SERVER = getenv("MY_SERVER", "bar_lo0o0o0o0o")
REPO_OWNER = getenv("REPO_OWNER", "bar_lo0o0")
MY_HEART = getenv("MY_HEART", "bar_lo0o0o0o0o")
BOT_UPDATE = getenv("BOT_UPDATE", "bar_lo0o0o0o0o")
MY_BRO = getenv("MY_BRO", "bar_lo0o0")
