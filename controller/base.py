from abc import ABC, abstractmethod
from aiogram import Dispatcher


class BaseController(ABC):
    @abstractmethod
    def register(self, dp: Dispatcher):
        pass
