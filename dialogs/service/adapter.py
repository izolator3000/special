from dialogs.service.user_data import User, TgDataAddress


def message2user(message, social_network):
    match social_network:
        case "telegram":
            data = [td.value for td in TgDataAddress]

            l = []
            for d in data:
                l.append(eval(d))
            # TODO Почему-то не работает строчка User(*[eval(td.value) for td in TgDataAddress])
            return User(*l)
        case _:
            print("Неизвестная соц сеть: ", message, social_network)

