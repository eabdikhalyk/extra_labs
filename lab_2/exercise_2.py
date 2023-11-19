number_of_lesson = int(input("Введите количество уроков от 1 до 10: "))
start_time = 9
duration = 45
short_break = 5
long_break = 15
result = 0
count = 0

while count < number_of_lesson:
    count += 1
    if count % 2 == 0:
         result += duration + long_break
    else:
         result += duration + short_break

if count % 2 == 0 :
    result = result - long_break
else:
    result = result - short_break

hour = int(result / 60)
minute = result % 60
print(f"{hour+start_time}:{minute}")