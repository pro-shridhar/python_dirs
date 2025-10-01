import datetime


def has_friday_13(month, year):
    day = datetime.date(year, month, 13)

    return day.strftime("%A") == "Friday"


print(has_friday_13(1, 1985))
