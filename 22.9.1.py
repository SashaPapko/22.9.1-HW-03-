def binary_search_in_list(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return low

def sort_list(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

user_input = input("Введите последовательность чисел через пробел:\
")
user_input = user_input.split()
try:
    user_input = [int(x) for x in user_input]
except ValueError:
    print("Ошибка ввода данных.")
    exit()

user_num = input("Введите любое число:\
")
try:
    user_num = int(user_num)
except ValueError:
    print("Ошибка ввода числа.")
    exit()

sorted_list = sort_list(user_input)
user_index = binary_search_in_list(sorted_list, user_num)

print("Исходная последовательность: ", user_input)
print("Сортированная последовательность: ", sorted_list)
print("Индекс элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу: ", user_index)
print("Элемент по найденному индексу: ", sorted_list[user_index])