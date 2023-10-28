list_num = []
list_sorted =[]
for i in range(1,4):
    list_num.append(int(input(f'Ввидите число {i}: ')))
swap = 0
for i in range(0,len(list_num)-1):
    for j in range(0,len(list_num)-1):
        if list_num[j] >= list_num[j+1]:
            swap = list_num[j]
            list_num[j] = list_num[j+1]
            list_num[j + 1] = swap

for i in list_num:
    print(i, end=' ')