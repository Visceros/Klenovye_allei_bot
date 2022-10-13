import json
import os
from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    bot_token: str
    mongo_url: str
    mongo_database: str
    fsm_mongo_database: str
    reply_chat: int
    presentation_copy_chat: int
    presentation_copy_message: int
    photo_copy_chat: int
    photo_copy_message: int
    tour_link: str
    support_chat_link: str
    webhook_enabled: bool
    webhook_url: str
    webhook_cert_file: str
    webhook_private_key_file: str
    webhook_app_host: str
    webhook_app_port: int

    def __init__(self):
        super().__init__(
            bot_token='5467209642:AAE2C0hK9W8ZaXqy1nB_t2smlliucqGiUho',
            mongo_url=os.getenv("DB_CONNECTION"),
            mongo_database=os.getenv("DB_DATABASE"),
            fsm_mongo_database=os.getenv("FSM_DATABASE"),
            reply_chat=406900953,
            presentation_copy_chat=1646022556,
            presentation_copy_message=7,
            photo_copy_chat=1646022556,
            photo_copy_message=6,
            tour_link=os.getenv("TOUR_LINK"),
            support_chat_link=os.getenv("SUPPORT_CHAT"),
            webhook_enabled=json.loads(os.getenv("WEBHOOK_ENABLED")),
            webhook_url=os.getenv("WEBHOOK_URL"),
            webhook_cert_file=os.getenv('WEBHOOK_CERT_FILE'),
            webhook_private_key_file=os.getenv('WEBHOOK_PRIVATE_KEY_FILE'),
            webhook_app_host=os.getenv("WEBHOOK_APP_HOST"),
            webhook_app_port=int(os.getenv("WEBHOOK_APP_PORT")),
        )
