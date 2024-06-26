from dialogs.service.user_data import TgDataAddress


def message2user(message, social_network):
    match social_network:
        case "telegram":
            d = {}
            for td in TgDataAddress:
                try:
                    d[str(td)[len("TgDataAddress."):]] = eval(td.value)
                except:
                    continue
            return d
        case _:
            print("Неизвестная соц сеть: ", message, social_network, sep='\n')

