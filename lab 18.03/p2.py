
"""Написать программу, выполняющую сортировку
списка целых чисел методом пирамидальной сортировки"""
def heapify(array,length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    """делаем правильность рсставления наших цифр"""
    if left < length and array[i] < array[left]:
        largest = left

    if right < length and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, length, largest)

def piramid_sort(array):
    length = len(array)

    for i in range(length // 2 - 1, -1):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j -1] = array[j - 1], array[j]
                return array
array = [1, 5, 7, 9, 2, 3, 6]
sorted_list = piramid_sort(array)
print(f"Отсортированный список {sorted_list}")