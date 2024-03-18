"""Написать программу, выполняющую сортировку
списка целых чисел методом быстрой сортировки."""
def quick_sort(arr):
    #Выбор пивота:
    if len(arr) <= 1:
        return arr
    #разделяем на подсписки и делаем рекрусивную сорировку
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

arr = [12, 11, 13, 5, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)

