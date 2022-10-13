from aiogram import Dispatcher
from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from . import BaseMarkupFactory


class StartMarkupFactory(BaseMarkupFactory):
    def __init__(self, support_chat_link: str):
        self.support_chat_link = support_chat_link

    def create(self) -> ForceReply | InlineKeyboardMarkup | ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn_callback = KeyboardButton(text='Заказать звонок')
        #btn_chat = KeyboardButton(text='Чат со специалистом')
        btn_presentation = KeyboardButton(text='Получить презентацию')
        #btn_come_to_see = KeyboardButton(text='Виртуальный тур')

        markup.row(btn_callback, btn_presentation)
        #markup.row(btn_chat, btn_come_to_see)
        return markup
