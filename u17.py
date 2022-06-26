numbers = list(map(int, input('Введите через пробел числа: \n').split()))
print('sequence_of_numbers', numbers, type(numbers))
element = int(input('Введите любое произвольное число: \n'))
print('element', element, type(element))
array = numbers + [element]
print('array', array, type(array))


def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print(merge_sort(array))
