raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "38-050-1234567",
    "    +38(050)123-32-34",
    "     0503451234. ",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "   44 245-2444. ",
]

import re


def normalize_phone(phone_number) -> str:   
# Нормалізує номер телефону до міжнародного формату.

    clean_phone = re.sub(r"[^\d+]", "", phone_number)

    if not re.search(r"\d", clean_phone):
        return ""

    if clean_phone.startswith("+"):
        return clean_phone
    elif clean_phone.startswith("380"):
        clean_phone = "+" + clean_phone
    elif clean_phone.startswith("0"):
        clean_phone = "+38" + clean_phone
    else:
        clean_phone = "+380" + clean_phone
   
    return clean_phone

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)