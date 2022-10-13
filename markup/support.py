from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

from . import BaseMarkupFactory


class SupportMarkupFactory(BaseMarkupFactory):
    def __init__(self, support_chat_link: str):
        self.support_chat_link = support_chat_link

    def create(self) -> ForceReply | InlineKeyboardMarkup | ReplyKeyboardMarkup:
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        btn_callback = InlineKeyboardButton(text='💬 Открыть чат', url=self.support_chat_link)
        markup.row(btn_callback)
        return markup
