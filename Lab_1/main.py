import datetime


def next_week(current_day):
    return current_day + datetime.timedelta(days=7)


today = datetime.date.today()

print(today)
next_week_day = next_week(today)
print(next_week_day)
print(next_week_day.strftime('%d'))
