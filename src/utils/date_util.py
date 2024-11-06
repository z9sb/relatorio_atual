from datetime import timedelta, date


def get_month_start():
    return (date.today() - timedelta(days=date.today().day)).replace(day=1)


def get_month_end():
    return (date.today() - timedelta(days=date.today().day))


if __name__ == "__main__":
    print(get_month_end())
