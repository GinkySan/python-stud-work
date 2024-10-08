import datetime

def get_week_number(date_obj):
    return date_obj.isocalendar()[1]

date_obj = datetime.datetime(2024, 10, 8)

week_number = get_week_number(date_obj)

print(week_number)