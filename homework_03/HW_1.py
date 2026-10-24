from datetime import datetime


def get_days_from_today(date) -> int | None : 
# Розраховує кількість днів між заданою датою і поточною датою.

    try:
        get_date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()

        difference_days = (today_date - get_date_obj).days  
        # int: Різниця в днях (негативне значення для дати у майбутньому)
        return difference_days  
    
    except ValueError:
        return None 

date = input("Введіть дату події в форматі YYYY-MM-DD: ") 

result = get_days_from_today(date)

if result is not None:
    print(f"Різниця між поточною та заданою датою: {result}")
else:
    print("Неможливо порахувати, введіть коректну дату")