def my_sort(my_list):
    even_list = []
    old_list = []
    for number in my_list:
        if isinstance(number, int):
            if number % 2 == 0:
                even_list.append(number)
            else:
                old_list.append(number)
    even_list.sort()
    old_list.sort()
    return old_list + even_list


my_data = [5, 8, 9, 12, 30, 1, 2, 50]
print(my_sort(my_data))