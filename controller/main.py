from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ContentType

from controller import BaseController
from markup import StartMarkupFactory, ContactMarkupFactory, SupportMarkupFactory


class PhoneReference(StatesGroup):
    presentation = State()
    tour = State()
    call = State()


class MainController(BaseController):
    def __init__(self, *, bot: Bot, presentation_copy_chat: int, presentation_copy_message: int,
                 tour_link: str, reply_chat: int, photo_copy_chat: int, photo_copy_message: int,
                 support_chat_link: str):
        self.bot = bot
        self.presentation_copy_chat = presentation_copy_chat
        self.presentation_copy_message = presentation_copy_message
        self.tour_link = tour_link
        self.reply_chat = reply_chat
        self.photo_copy_chat = photo_copy_chat
        self.photo_copy_message = photo_copy_message
        self.support_chat_link = support_chat_link


    # Для отправки перезентации с запросом телефона

    # async def _send_presentation(self, chat_id: int, phone_number: str, full_name: str):
    #     await self.bot.send_message(chat_id=self.reply_chat,
    #                                 text=f'<a href="tg://user?id={chat_id}">'
    #                                      f'{full_name}</a> '
    #                                      f'с номером телефона: <code>{phone_number}</code> '
    #                                      f'запросил презентацию', parse_mode="HTML")
    #     # доп пересылка директору
    #     await self.bot.send_message(chat_id=358615049,
    #                                 text=f'<a href="tg://user?id={chat_id}">'
    #                                      f'{full_name}</a> '
    #                                      f'с номером телефона: <code>{phone_number}</code> '
    #                                      f'запросил презентацию', parse_mode="HTML")
    #
    #     await self.bot.copy_message(chat_id, self.presentation_copy_chat, self.presentation_copy_message,
    #                                 reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())


    # Отправка вирт тура С запросом телефона

    # async def _send_tour(self, chat_id: int, phone_number: str, full_name: str):
    #     await self.bot.send_message(chat_id=self.reply_chat,
    #                                 text=f'<a href="tg://user?id={chat_id}">'
    #                                      f'{full_name}</a> '
    #                                      f'с номером телефона: <code>{phone_number}</code> '
    #                                      f'запросил виртуальный тур', parse_mode="HTML")
    #     await self.bot.send_message(chat_id, f"Ссылка на тур: {self.tour_link}",
    #                                 reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())


    # Для отправки перезентации БЕЗ запроса телефона

    async def _send_presentation(self, chat_id: int, full_name: str):
        await self.bot.send_message(chat_id=self.reply_chat,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'запросил презентацию', parse_mode="HTML")
        await self.bot.copy_message(chat_id, self.presentation_copy_chat, self.presentation_copy_message,
                                    reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())
        # доп пересылка директору
        await self.bot.send_message(chat_id=358615049,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'запросил презентацию', parse_mode="HTML")
        # доп пересылка Кристине
        await self.bot.send_message(chat_id=451859607,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'запросил презентацию', parse_mode="HTML")

    # Отправка вирт тура БЕЗ запроса телефона

    # async def _send_tour(self, chat_id: int, full_name: str):                # Убран запрос номера телефона
    #     await self.bot.send_message(chat_id=self.reply_chat,
    #                                 text=f'<a href="tg://user?id={chat_id}">'
    #                                      f'{full_name}</a> '
    #                                      f'запросил виртуальный тур', parse_mode="HTML")
    #     await self.bot.send_message(chat_id, f"Ссылка на тур: {self.tour_link}",
    #                                 reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())
        # доп пересылка директору

        # await self.bot.send_message(chat_id=358615049,
        #                            text=f'<a href="tg://user?id={chat_id}">'
        #                                 f'{full_name}</a> '
        #                                 f'запросил виртуальный тур', parse_mode="HTML")
        #
        # # доп пересылка Кристине
        # await self.bot.send_message(chat_id=451859607,
        #                             text=f'<a href="tg://user?id={chat_id}">'
        #                                  f'{full_name}</a> '
        #                                  f'запросил виртуальный тур', parse_mode="HTML")

    async def _send_recall(self, chat_id: int, phone_number: str, full_name: str):
        await self.bot.send_message(chat_id=self.reply_chat,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'с номером телефона: <code>{phone_number}</code> '
                                         f'<b>нужно перезвонить</b>', parse_mode="HTML")
        # доп пересылка директору
        await self.bot.send_message(chat_id=358615049,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'с номером телефона: <code>{phone_number}</code> '
                                         f'<b>нужно перезвонить</b>', parse_mode="HTML")

        # доп пересылка Кристине
        await self.bot.send_message(chat_id=451859607,
                                    text=f'<a href="tg://user?id={chat_id}">'
                                         f'{full_name}</a> '
                                         f'с номером телефона: <code>{phone_number}</code> '
                                         f'<b>нужно перезвонить</b>', parse_mode="HTML")

        await self.bot.send_message(chat_id, f"Спасибо! В скором времени наш менеджер позвонит вам",
                                    reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())


    async def _request_contact(self, chat_id: int, reason: State, message: str):
        await reason.set()
        await self.bot.send_message(chat_id=chat_id, text=message, reply_markup=ContactMarkupFactory().create())


    async def on_start(self, message: Message, state: FSMContext):
        await state.reset_state()
        await self.bot.copy_message(chat_id=message.from_user.id, from_chat_id=self.photo_copy_chat,
                                    message_id=self.photo_copy_message,
                                    caption=f"Добрый день {message.from_user.full_name}! "
                                            f"Это чат-бот ЖК «Кленовые аллеи», мы на связи!\n\n"
                                            "Жилой комплекс «Кленовые Аллеи» - это готовые квартиры в центре Новой Москвы от надёжного застройщика ГК МИЦ."
                                            " Комплекс находится в 3 минутах пешком от станции метро «Кедровая» и всего в 12 минутах пути от МКАД по Калужскому шоссе. Московская прописка!\n\n"
                                            "В продаже последние квартиры от 8,2 млн. рублей. "
                                            "Ипотека от 1% для всех на весь срок кредита.\nДо 31 октября действует скидка до 7% на покупку.",
                                    reply_markup=StartMarkupFactory(support_chat_link=self.support_chat_link).create())

    async def on_presentation_text_phone(self, message: Message, state: FSMContext):
        msg = message.text.strip()
        if msg.startswith('+') or msg[0].isdigit():
            if msg[1:].isdigit():
                phone = message.text

                await state.update_data(phone=phone)
                await self._send_presentation(chat_id=message.from_user.id, phone_number=phone, full_name=message.from_user.full_name)
                await state.finish()

        else:
            await self._request_contact(message.from_user.id, PhoneReference.presentation,
                                    message="Не удалось распознать номер телефона. Пожалуйста, проверьте корректность номера и введите ещё раз, или отправьте номер телефона с помощью специальной кнопки внизу.")

    async def on_call_text_phone(self, message: Message, state: FSMContext):
        msg = message.text.strip()
        if msg.startswith('+') or msg[0].isdigit():
            if msg[1:].isdigit():
                phone = message.text

                await state.update_data(phone=phone)
                await self._send_recall(chat_id=message.from_user.id, phone_number=phone,
                                              full_name=message.from_user.full_name)
                await state.finish()

        else:
            await self._request_contact(message.from_user.id, PhoneReference.call,
                                        message="Не удалось распознать номер телефона. Пожалуйста, проверьте корректность номера и введите ещё раз, или отправьте номер телефона с помощью специальной кнопки внизу.")

    # async def on_tour_text_phone(self, message: Message, state: FSMContext):
    #     msg = message.text.strip()
    #     if msg.startswith('+') or msg[0].isdigit():
    #         if msg[1:].isdigit():
    #             phone = message.text
    #
    #             await state.update_data(phone=phone)
    #             await self._send_tour(chat_id=message.from_user.id, phone_number=phone,
    #                                           full_name=message.from_user.full_name)
    #             await state.finish()
    #
    #     else:
    #         await self._request_contact(message.from_user.id, PhoneReference.call,
    #                                     message="Не удалось распознать номер телефона. Пожалуйста, проверьте корректность номера и введите ещё раз, или отправьте номер телефона с помощью специальной кнопки внизу.")


    async def on_support_chat(self, message: Message):
        await message.answer("Связаться с нами 👇",
                             reply_markup=SupportMarkupFactory(support_chat_link=self.support_chat_link).create())

    # async def on_tour(self, message: Message, state: FSMContext):  # Отправка вирт тура с запросом номера телефона
    #     fsm_data = await state.get_data()
    #     have_number = "phone" in fsm_data
    #     if have_number:
    #         await self._send_tour(message.from_user.id, phone_number=fsm_data["phone"],
    #                               full_name=message.from_user.full_name)
    #     else:
    #         await self._request_contact(message.from_user.id, PhoneReference.tour,
    #                                     "Для получения ссылки на просмотр, пожалуйста, оставьте ваш номер телефона.")

    # async def on_tour(self, message: Message, state: FSMContext): # Отправка вирт тура БЕЗ запроса номера телефона
    #     fsm_data = await state.get_data()
    #     await self._send_tour(message.from_user.id, full_name=message.from_user.full_name)

    # async def on_presentation(self, message: Message, state: FSMContext):  # Отправка презентации с запросом номера телефона
    #     fsm_data = await state.get_data()
    #     have_number = "phone" in fsm_data
    #     if have_number:
    #         await self._send_presentation(message.from_user.id, phone_number=fsm_data["phone"],
    #                                       full_name=message.from_user.full_name)
    #     else:
    #         await self._request_contact(message.from_user.id, PhoneReference.presentation,
    #                                     "Для получения презентации, пожалуйста, оставьте ваш номер телефона.")

    async def on_presentation(self, message: Message, state: FSMContext):  # Отправка презентации БЕЗ запроса номера телефона
        await self._send_presentation(message.from_user.id, full_name=message.from_user.full_name)

    async def on_recall(self, message: Message, state: FSMContext):
        fsm_data = await state.get_data()
        have_number = "phone" in fsm_data
        if have_number:
            await self._send_recall(message.from_user.id, phone_number=fsm_data["phone"],
                                    full_name=message.from_user.full_name)
        else:
            await self._request_contact(message.from_user.id, PhoneReference.call,
                                        "Для заказа звонка, пожалуйста, оставьте ваш номер телефона.")

    async def on_cancel(self, message: Message, state: FSMContext):
        await state.finish()
        await state.reset_state()
        await self.on_start(message, state=state)

    # async def on_contact_tour(self, message: Message, state: FSMContext):
    #     await self._send_tour(message.from_user.id, phone_number=message.contact.phone_number,
    #                           full_name=message.from_user.full_name)
    #     await state.finish()
    #
    #     await state.update_data(phone=message.contact.phone_number)

    async def on_contact_call(self, message: Message, state: FSMContext):
        await self._send_recall(message.from_user.id, phone_number=message.contact.phone_number,
                                full_name=message.from_user.full_name)
        await state.finish()

        await state.update_data(phone=message.contact.phone_number)

    async def on_contact_presentation(self, message: Message, state: FSMContext):
        await self._send_presentation(message.from_user.id, phone_number=message.contact.phone_number,
                                      full_name=message.from_user.full_name)
        await state.finish()

        await state.update_data(phone=message.contact.phone_number)

    def register(self, dp: Dispatcher):
        dp.register_message_handler(self.on_start, commands=["start", "help"], state="*")
        dp.register_message_handler(self.on_cancel, Text(equals='Отмена'), state="*")
        dp.register_message_handler(self.on_support_chat, Text(equals='Чат со специалистом'))
#        dp.register_message_handler(self.on_tour, Text(equals='Виртуальный тур'))
        dp.register_message_handler(self.on_presentation, Text(equals='Получить презентацию'))
        dp.register_message_handler(self.on_recall, Text(equals='Заказать звонок'))
#        dp.register_message_handler(self.on_contact_tour, content_types=[ContentType.CONTACT], state=PhoneReference.tour)
        dp.register_message_handler(self.on_contact_call, content_types=[ContentType.CONTACT],
                                    state=PhoneReference.call)
        dp.register_message_handler(self.on_contact_presentation, content_types=[ContentType.CONTACT],
                                    state=PhoneReference.presentation)
        dp.register_message_handler(self.on_call_text_phone, state=PhoneReference.call)
#        dp.register_message_handler(self.on_tour_text_phone, state=PhoneReference.tour)
        dp.register_message_handler(self.on_presentation_text_phone, state=PhoneReference.presentation)
