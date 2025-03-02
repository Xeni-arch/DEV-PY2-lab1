import doctest
from typing import Union

class Weather:
    def __init__(self, selected_days: int, sunny_days: int, cloudy_days: int):
        """
        Создание и подготовка к работе объекта "Погода"

        :param selected_days: Количество дней
        :param sunny_days: Количество солнечных дней
        :param cloudy_days: Количество пасмурных дней

        Примеры:
        >>> weather = Weather(15, 5, 10)  # инициализация экземпляра класса
        """
        if not isinstance(selected_days, int):
            raise TypeError("Количество дней должно быть типа int")
        if selected_days < 0:
            raise ValueError("Количество дней должно быть положительным числом")
        self.selected_days = selected_days

        if not isinstance(sunny_days, int):
            raise TypeError("Количество солнечных дней должно быть типа int")
        if sunny_days < 0:
            raise ValueError("Количество солнечных дней должно быть положительным числом")
        self.sunny_days = sunny_days

        if not isinstance(cloudy_days, int):
            raise TypeError("Количество пасмурных дней должно быть типа int")
        if cloudy_days < 0:
            raise ValueError("Количество пасмурных дней должно быть положительным числом")
        self.cloudy_days = cloudy_days

        if cloudy_days + sunny_days > selected_days:
            raise TypeError("Количество дней должно быть равно сумме солнечных и пасмурных дней")

    def is_weather_good(self) -> None:
        """
        Функция которая проверяет является ли погода хорошей

        :return: Является ли погода хорошей

        Примеры:
        >>> weather = Weather(15, 5, 10)
        >>> weather.is_weather_good()
        """
        ...

    def is_rain_possible(self) -> None:
        """
        Функция которая проверяет возможен ли дождь

        :return: Возможен ли дождь

        Примеры:
        >>> weather = Weather(15, 5, 10)
        >>> weather.is_rain_possible()
        """
        ...

class Account:
    def __init__(self, amount_of_money: Union[int, float], username: str):
        """
        Создание и подготовка к работе объекта "Счет в банке"

        :param amount_of_money: Количество денег
        :param username: Имя клиента банка
        Примеры:
        >>> account = Account(15000, "Анна")  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_money, (int, float)):
            raise TypeError("Количество денег должно быть типа int или float")
        if amount_of_money < 0:
            raise ValueError("Количество денег должно быть положительным числом")
        self.amount_of_money = amount_of_money

        if not isinstance(username, str):
            raise TypeError("Количество пасмурных дней должно быть типа str")
        if len(username) < 0:
            raise ValueError("Имя пользователя должно иметь не менее 1 символа")
        self.username = username

    def add_money(self, add_money: Union[int, float]):
        """
        Добавление средств на счет

        :return: Итоговый счет
        :param add_money: Количество добавленных средств

        Примеры:
        >>> account = Account(15000, "Анна")
        >>> account.add_money(200)
        """
        if not isinstance(add_money, (int, float)):
            raise TypeError("Добавляемое количество денег на счет должно быть типа int или float")
        if add_money < 0:
            raise ValueError("Добавляемое количество средств на счет не может быть отрицательным числом")

    def remove_money(self, remove_money: Union[int, float]):
        """
        Снятие денег со счета

        :return: Итоговый счет
        :param add_money: Количество снимаемых средств

        Примеры:
        >>> account = Account(15000, "Анна")
        >>> account.remove_money(200)
        """
        if not isinstance(remove_money, (int, float)):
            raise TypeError("Снимаемое количество денег на счет должно быть типа int или float")
        if remove_money < 0:
            raise ValueError("Снимаемое количество средств на счет не может быть отрицательным числом")

class Bookshelf:
    def __init__(self, number_of_books: int, maximum_books: int):
        """
        Создание и подготовка к работе объекта "Книжная полка"

        :param number_of_books: Количество книг
        :param maximum_books: Максимальное количество книг на полке

        Примеры:
        >>> bookshelf = Bookshelf(2, 10)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_books, int):
            raise TypeError("Количество книг на полке должно быть типа int")
        if number_of_books < 0:
            raise ValueError("Количество книг на полке должно быть положительным числом")
        self.number_of_books = number_of_books

        if not isinstance(maximum_books, int):
            raise TypeError("Максимальное количество книг на полке должно быть типа int")
        if maximum_books < 0:
            raise ValueError("Максимальное количество книг на полке должно быть положительным числом")
        self.maximum_books = maximum_books

        if number_of_books > maximum_books:
            raise TypeError("Количество книг на полке не должно быть больше максимальной вместимости полки")

    def add_books(self, add_books: int):
        """
        Добавление книг на полку

        :return: Итоговое количество книг
        :param add_books: Количество добавленных книг

        Примеры:
        >>> bookshelf = Bookshelf(2, 10)
        >>> bookshelf.add_books(1)
        """
        if not isinstance(add_books, int):
            raise TypeError("Добавляемое количество книг должно быть типа int")
        if add_books < 0:
            raise ValueError("Добавляемое количество книг не может быть отрицательным числом")

    def remove_books(self, remove_books: int):
        """
        Снятие книг с полки

        :return: Итоговое количество книг
        :param remove_books: Количество убранных книг

        Примеры:
        >>> bookshelf = Bookshelf(2, 10)
        >>> bookshelf.remove_books(1)
        """
        if not isinstance(remove_books, int):
            raise TypeError("Количество убранных книг должно быть типа int")
        if remove_books < 0:
            raise ValueError("Количество убранных книг не может быть отрицательным числом")

if __name__ == "__main__":
    doctest.testmod()