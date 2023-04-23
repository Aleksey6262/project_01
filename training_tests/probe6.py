
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
# for перебирающий эелементы
for item in shop_list:
    print(item)

# for перебирающий индексы
for ind in range(len(shop_list)):
    print(ind)

# for и enumerate()
for ind, item in enumerate(shop_list):
    print(ind, item)

# while перебирающий индексы
ind = 0
while ind < len(shop_list):
    print(shop_list[ind])
    ind += 1

