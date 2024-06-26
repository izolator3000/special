from enum import Enum
from collections import namedtuple


class Cash(Enum):
    START_START = "Привет! Ты разговариваешь с помощником студии бальных причесок и макияжа Special"
    CLIENT_NAME = "Как тебя зовут?"
    PHONE = "Введите контактный номер телефона, по которому можно с вами будет связываться"
    STANDARD_START = "Записаться хочешь, или узнать цену"
    STST_FIND_PRICE = "Узнать цену"
    STST_ORDER = "Записаться"
    STST_PAY = "Оплатить"
    IF_CHILD = "Напиши имя и фамилию ребенка"
    SEX = "Пол ребенка"
    TOURNAMENT = "На каком турнире примите участие?"
    TOUR_PART = "Во сколько начало? Время вашего первого отделения"
    HAIRSTYLE = "Какую прическу хотите?"
    PHOTO_M = "Фото волос: вид сбоку сверху"
    PHOTO_G = "Фото волос сзади. Длина какая?"
    COMMENT = "Комментарий к прическе есть?"
    THX = "Спасибо, что обратились к нам. Накануне турнира вы получите напоминание:)"
    WHAT_HELL = "Что хочешь?"
    SELF_OR_CHILD = "Кому узнать цену: себе или ребенку?"
    LINK2PAY = "Перейдите по этой ссылке и оплатите прическу " \
               "https://www.sberbank.com/sms/pbpn?requisiteNumber=79817325883"

MyMessage = namedtuple("Message", "chat_id text reply_markup")
