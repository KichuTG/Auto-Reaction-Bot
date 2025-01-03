from os import environ as env

class Telegram:
    API_ID = int(env.get("API_ID", "28714959"))
    API_HASH = env.get("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
    BOT_TOKEN = env.get("BOT_TOKEN", "7790394927:AAF1P6G36iH5XFY7N9Df9OOWmrfKxt68UB8")
    BOT_USERNAME = env.get("BOT_USERNAME", "TGReact1bot")
    EMOJIS = [
        "👍", "🙃", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤭", "😢",
        "🥶", "🤩", "😮", "😻",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "😸", "🏆",
        "🫠", "🤨", "😐", "❤️‍🔥",
        "👅", "🆒", "😼", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
