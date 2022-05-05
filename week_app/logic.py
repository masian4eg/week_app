import datetime


def which_week(day, month, year):
    week = 0  # создаем счетчик недель

    try:
        if year == 2019:  # условие выполнение кода, если введена дата 2019 года
            week = int(datetime.date(year, month, day).strftime("%U"))

        elif year == 2020:  # условие выполнение кода, если введена дата 2020 года
            week = int(datetime.date(year, month, day).strftime("%U")) + 53

        elif year == 2021:  # условие выполнение кода, если введена дата 2021 года
            week = int(datetime.date(year, month, day).strftime("%U")) + 53 * 2

        elif year == 2022:  # условие выполнение кода, если введена дата 2022 года
            week = int(datetime.date(year, month, day).strftime("%U")) + 53 * 3

        elif year >= 2023 or year <= 2018:  # если дата вне диапазона 2019-2022 годов
            return 'Введена не верная дата. Введите любую дату в промежутке 2019-2022 годов'

    except TypeError:  # если введены данные другого типа данных отличные от int
        return 'Не верный формат даты'

    except ValueError:  # если введены данные больше или меньше существующих дат
        return 'Не верный формат чисел'

    else:  # подсчет номера недели
        return f'Номер недели\n{week + 1}'