my_dict = {'Kate': 1991, 'Mary': 1990, 'Andrey': 1995}   # словарь
print("Dict:", my_dict)
print("Existing value:", my_dict['Kate'])                # значение по ключу
print("Not existing value:", my_dict.get('Helen'))       # значение-проверка по ключу, отсутствующее значение
my_dict.update({'Ann': 2003, 'Alex': 1991})              # добавление нескольких значений
a = my_dict.pop('Mary')                                  # удаление элемента с сохранением значения в форме переменной
print("Deleted value: ", a)                               # извлеченное значение
print("Modified dictionary:", my_dict)                   # обновлённый словарь

my_set = {1, 2, 'a', 3.14, 2, 1, 3, 3.14}            # множество
print("Set:", my_set)
my_set.update({'b','c'})                             # добавление группы эл.
my_set.remove(3.14)                                  # удаление эл.
print("Modified set:", my_set)                       # обновлённое множество