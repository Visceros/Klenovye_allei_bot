from abc import ABC, abstractmethod
from aiogram import Dispatcher
from aiogram.types import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup


class BaseMarkupFactory(ABC):
    @abstractmethod
    def create(self) -> ForceReply | InlineKeyboardMarkup | ReplyKeyboardMarkup:
        pass
