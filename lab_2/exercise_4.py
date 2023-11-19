list_num = []

for i in range(1,4):
    list_num.append(int(input(f'Ввидите число {i}: ')))
    
max=list_num[0]

for num in list_num:
    if num > max:
        max = num

print(f"max: {max}")