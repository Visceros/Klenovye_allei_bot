from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from . import BaseMarkupFactory


class ContactMarkupFactory(BaseMarkupFactory):
    def create(self) -> ForceReply | InlineKeyboardMarkup | ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn_contact = KeyboardButton(text='Отправить номер телефона', request_contact=True)
        btn_cancel = KeyboardButton(text='Отмена')

        markup.row(btn_contact)
        markup.row(btn_cancel)
        return markup
