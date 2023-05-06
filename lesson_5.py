#Множества set, frozenset
# numbers = {1, 2, 3, 4, 5, "5"}
# print(numbers)
# print(numbers[0:2])

# it_company = {"Google", "Meta", "Space X"}
# print(it_company)
# it_company.add("Tesla")
# print(it_company)
# it_company.remove("Google")
# print(it_company)
# it_company.pop()
# print(it_company)

# st = {1, 0.1, "Hello", False, (1, 2, 3)} #list, set - нельзя хранить
# print(st)

# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]
# nums3 = nums1 + nums2
# print(list(set(nums3)))

# cars = {"BMW", "DODGE", "TESLA", "HONDA"}
# for car in cars:
#     print(car)

# numbers = {1, 0.1, 100, 4, 99, 1111, 9, 8, 34}
# print(sorted(numbers))

# st = {1, 1.0, True, "1"}
# print(st)
# print(False + 1)

# frozen_set = frozenset({1, 2, 3, 4, 5, 5, 5})
# print(frozen_set)
# frozen_set.add("Tesla")

#Dictionary - Словари
# student = {'name' : 'Askhat', 'age' : 18}
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python')
# print(student)
# student.pop('age')
# print(student)
# student['language'] = 'Java'
# print(student)

# tesla_model_x = {
#     'brand' : 'Tesla',
#     'model' : 'Model X',
#     'year' : 2022,
#     'price' : '46000$',
#     'color' : 'white'
# }
# print(tesla_model_x['brand'])
# print(tesla_model_x.keys())
# print(tesla_model_x.values())
# print(tesla_model_x.items())
# for key, value in tesla_model_x.items():
#     print(key, value)

todo_list = {
    '08:00' : 'Проснуться'
}
while True:
    command = int(input("Введите комманду, 1 - посмотреть список дел, 2 - добавить, 3 - удалить: "))
    if command == 1:
        print("СПИСОК ДЕЛ:")
        for time, task in todo_list.items():
            print(time, task)
        print("--------------------------------------")
    elif command == 2:
        add_time = input("Время: ")
        add_task = input("Задание: ")
        todo_list.setdefault(add_time, add_task)
        print("Задание", add_task, "успешно добавлена на", add_time)
        print("--------------------------------------")
    elif command == 3:
        delete_time = input("Введите время для удаления: ")
        todo_list.pop(delete_time)
        print("Задание удалено")
        print("--------------------------------------")
    elif command == 0:
        print("EXIT TODO")
        break
    else:
        print("Такой комманды нету")