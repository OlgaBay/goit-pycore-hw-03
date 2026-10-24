from datetime import datetime, date, timedelta


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Brown", "birthday": "1978.02.14"},
    {"name": "Emily Johnson", "birthday": "1992.02.20"},
    {"name": "David Wilson", "birthday": "1988.03.08"},
    {"name": "Sarah Davis", "birthday": "1995.04.17"},
    {"name": "Robert Miller", "birthday": "1982.05.30"},
    {"name": "Olivia Taylor", "birthday": "2000.06.12"},
    {"name": "James Anderson", "birthday": "1975.07.04"},
    {"name": "Sophia Thomas", "birthday": "1998.08.21"},
    {"name": "Daniel Jackson", "birthday": "1987.09.15"},
    {"name": "Emma White", "birthday": "1993.10.25"},
    {"name": "William Harris", "birthday": "1980.10.29"},
    {"name": "Isabella Martin", "birthday": "1996.12.30"},
    {"name": "Alexander Clark", "birthday": "1991.12.31"}
]

def get_upcoming_birthdays(users):    
# Повертає список найближчих днів народження з урахуванням вихідних

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        name = user["name"]

        birthday_this_year = birthday.replace(year=today.year)   

        # Перевіряє, чи вже минув день народження в цьому році 
        if birthday_this_year < today:                          
            birthday_this_year = birthday_this_year.replace(year=today.year+1)

        birthday_weekday = birthday_this_year.weekday()  

        # Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
        if birthday_weekday == 5:
            celebrate_day = birthday_this_year + timedelta(days=2)
        elif birthday_weekday == 6:
            celebrate_day = birthday_this_year + timedelta(days=1)
        else:
            celebrate_day = birthday_this_year

        celebrate_day = celebrate_day.strftime("%Y.%m.%d")

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": celebrate_day
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)