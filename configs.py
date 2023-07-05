from dotenv import load_dotenv
import os
from enum import Enum


class Configs:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.bot_token = os.getenv('BOT_TOKEN')
        self.api_id = os.getenv('API_ID')
        self.api_hash = os.getenv('API_HASH')
        self.mongo_url = os.getenv('MONGO_URL')
        self.channel_id = os.getenv("CHANNEL_ID")
        if self.channel_id:
            self.channel_id = int(self.channel_id)


class Subscription(Enum):
    FREE = 0
    PRO = 1
    ULTIMATE = 2

configs = Configs()
