from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton  # , ReplyKeyboardRemove


def create_keyboard(buttons: tuple, layout_method: tuple, reply=True):
    if reply:
        return _reply_keyboard(buttons, layout_method)
    else:
        return _inline_keyboard(buttons)


def _inline_keyboard(buttons: tuple):
    builder = InlineKeyboardBuilder()
    for i, text_but in enumerate(buttons):
        builder.add(InlineKeyboardButton(text=text_but, callback_data=str(i)))
    return builder


def _reply_keyboard(buttons_texts: tuple[str], layout_method: tuple):
    keyboard = []

    for row in range(len(layout_method)):
        keyboard.append([])
        x = sum(layout_method[:row])
        keyboard[row].append(KeyboardButton(text=buttons_texts[x]))
        for but in range(x + 1, x + layout_method[row]):
            keyboard[row].append(KeyboardButton(text=buttons_texts[but]))
    # input_field_placeholder="Мой собственный текст"
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)


def request_phone():
    button = KeyboardButton(text='Поделиться телефоном', request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True, one_time_keyboard=True)

# def keyboard_inline(self, task):  # Создание клавиатур для турнира и отделения
#     keyboard = InlineKeyboardMarkup()
#     if task == "Кнопки турниров":
#         for tour_times in self.tournaments_starts_dance:
#             keyboard.add(InlineKeyboardButton(tour_times[0], callback_data=f'Tour{tour_times[0]}'))
#
#     elif task.startswith("Tour"):
#         for tour_start in self.tournaments_starts_dance:
#             if tour_start[0] == task[4:]:
#                 for time in tour_start[1].replace(' ', '').split(','):
#                     keyboard.add(InlineKeyboardButton(time, callback_data=f'Start{time}'))
#                 break
#     elif task == "hairstyleg":
#         for hair in tuple(zip(*self.excel.get_hairstyle_list()))[1]:
#             if len(hair) < 30:
#                 keyboard.add(InlineKeyboardButton(hair, callback_data=f'hair{hair}'))
#     elif task == "hairstylem":
#         for hair in tuple(zip(*self.excel.get_hairstyle_list()))[0]:
#             if len(hair) < 30:
#                 keyboard.add(InlineKeyboardButton(hair, callback_data=f'hair{hair}'))
#     return keyboard
