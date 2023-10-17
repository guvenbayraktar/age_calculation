from datetime import datetime
from datetime import timedelta

"""
birthday = input("Dogum tarihinizi Gun.Ay.Yil olacak şekilde giriniz.: ")
birthday = datetime.strptime(birthday, "%d.%m.%Y")
birthday = birthday.date()
print(birthday)

current_date = datetime.today()
current_date = current_date.date()
print(current_date)

age = current_date - birthday

year = age.days // 365.25
month = age.days % 365.25 // 30.4375
day = age.days % 365.25 % 30.4375

print(f'Yasiniz: {int(year)} yil, {int(month)} ay, {int(day)} gün')
"""

def age_calculate():

    birthday = input("Dogum tarihinizi Gun.Ay.Yil olacak şekilde giriniz.: ")
    birthday = datetime.strptime(birthday, "%d.%m.%Y")
    birthday = birthday.date()
    print(birthday)

    current_date = datetime.today()
    current_date = current_date.date()
    print(current_date)

    age = current_date - birthday

    year = age.days // 365.25
    month = age.days % 365.25 // 30.4375
    day = age.days % 365.25 % 30.4375

    return print(f'Yasiniz: {int(year)} yil, {int(month)} ay, {int(day)} gün')

age_calculate()
