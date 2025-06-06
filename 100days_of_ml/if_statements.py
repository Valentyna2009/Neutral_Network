temperature_list = [3, 16, -2, 21, 30, 15, 1, -5, 24, 27]

freezing = []
cold = []
warm = []
hot = []

for i in temperature_list:
    if i < 0:
        freezing.append(i)
    elif 0 <= i <= 15:
        cold.append(i)
    elif 16 <= i <= 25:
        warm.append(i)
    else:
        hot.append(i)

print('Freezing: ' + ', '.join(str(num) for num in freezing))
print('Cold: ' + ', '.join(str(num) for num in cold))
print('Warm: ' + ', '.join(str(num) for num in warm))
print('Hot: ' + ', '.join(str(num) for num in hot))

steps_list = [10000, 2300, 4350, 5671, 932]

for x in steps_list:
    if 0 <= x <= 4999:
        category = 'non_active'
    elif 5000 <= x <= 7499:
        category = 'light_active'
    elif 7500 <= x <= 9999:
        category = 'middle_active'
    else:
        category = 'super_active'

    print(f"Steps: {x}; category: {category}")