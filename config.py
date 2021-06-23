import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1802997328:AAHE-LLyvliJo-X9yY0w40yCTn0BUx8bn1g")

    APP_ID = int(os.environ.get("APP_ID", "5799454")

    API_HASH = os.environ.get("API_HASH", "0116b6e4220e6d4c22f86ed7cf26d203")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")
