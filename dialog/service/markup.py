from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # , ReplyKeyboardRemove


class Markup:
    def __init__(self):
        pass # self.tournaments_starts_dance = self.excel.get_tours_starts()

    def keyboard_inline(self, task):    # Создание клавиатур для турнира и отделения
        keyboard = InlineKeyboardMarkup()
        if task == "Кнопки турниров":
            for tour_times in self.tournaments_starts_dance:
                keyboard.add(InlineKeyboardButton(tour_times[0], callback_data=f'Tour{tour_times[0]}'))

        elif task.startswith("Tour"):
            for tour_start in self.tournaments_starts_dance:
                if tour_start[0] == task[4:]:
                    for time in tour_start[1].replace(' ', '').split(','):
                        keyboard.add(InlineKeyboardButton(time, callback_data=f'Start{time}'))
                    break
        elif task == "hairstyleg":
            for hair in tuple(zip(*self.excel.get_hairstyle_list()))[1]:
                if len(hair) < 30:
                    keyboard.add(InlineKeyboardButton(hair, callback_data=f'hair{hair}'))
        elif task == "hairstylem":
            for hair in tuple(zip(*self.excel.get_hairstyle_list()))[0]:
                if len(hair) < 30:
                    keyboard.add(InlineKeyboardButton(hair, callback_data=f'hair{hair}'))
        return keyboard

    def create_keyboard(self, buttons: tuple, layout_method: tuple, inline=True):
        if inline:
            return self._inline_keyboard(buttons, layout_method)
        else:
            return self._reply_keyboard(buttons)

    def _reply_keyboard(self, buttons: tuple): pass     # TODO: доделать клавиатуру


    def _inline_keyboard(self, buttons: tuple, layout_method: tuple):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        # input_field_placeholder="Мой собственный текст"
        for i in range(len(layout_method)):
            x = sum(layout_method[:i])
            keyboard.add(KeyboardButton(buttons[x]))
            for j in range(x + 1, x + layout_method[i]):
                keyboard.insert(KeyboardButton(buttons[j]))

        return keyboard

    def request_phone(self):
        button = KeyboardButton('Поделиться телефоном', request_contact=True)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(button)
        return keyboard