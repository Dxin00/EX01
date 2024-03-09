from datetime import datetime, timedelta          
from collections import defaultdict

users = [
    {"name": "Jack Robinson", "birthday": datetime(1982, 1, 24)},
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 10)},
    {"name": "Jan Koum", "birthday": datetime(1976, 3, 12)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 3, 15)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 14)},
]

def birth_week(users):
    today = datetime.today().date()
    birth_per_day = {"Monday" : [],
                    "Tuesday" : [],
                    "Wednesday" : [],
                    "Thursday" : [],
                    "Friday" : [],
                    }

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birth_this_year = birthday.replace(year=today.year)

        if birth_this_year < today:
            birth_this_year = birth_this_year.replace(year=today.year + 1)

        delta_days = (birth_this_year - today).days

        if delta_days < 7:
            day_of_week = birth_this_year.strftime("%A")
            if day_of_week in ("Saturday", "Sunday"):
                birth_per_day["Monday"].append(name)
            else:
                birth_per_day[day_of_week].append(name)

    result_string = ""
    for day, names in birth_per_day.items():
        if names:
            result_string += f"{day}: {', '.join(names)}\n"

    return result_string

print(birth_week(users))
