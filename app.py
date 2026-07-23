from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# Example
birth = date(2005, 8, 15)
print(f"Your age is {calculate_age(birth)} years.")