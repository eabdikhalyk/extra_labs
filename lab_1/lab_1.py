import datetime as dt

print("Здравствуйте, вы проходите анкету")

first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилия: ")
birthday = int(input("Введите ваш год рождения: "))
do_you_like_course = input("Нравится ли вам курс? ")
what_is_yor_expectation_from_course = input("Что вы ожидаете в дальнейних занаятиях? ")

current_year = dt.datetime.now().year

print("\n")
print("Вы заполнили такие данные: ")
print(f"Bac зовут: {first_name} {last_name}")
print(f"Вам {current_year - birthday} лет")
print(f"Ваш ответ к первому вопросу: {do_you_like_course}")
print(f"Ваш ответ к второму вопросу: {what_is_yor_expectation_from_course}")

