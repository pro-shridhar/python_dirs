def format_date(date):
    month, day, year = date.split("/")
    return f"{year}{day}{month}"


print(format_date("23/345/45"))
