list_num = []
list_equal =[]
for i in range(1,4):
    list_num.append(int(input(f'Ввидите число {i}: ')))

for i in range(0,len(list_num)):
    for j in range(0,len(list_num)):
        if i != j:
            if list_num[i] == list_num[j]:
                if len(list_num) == len(list_equal):
                    break
                list_equal.append(list_num[i])


print(len(list_equal))