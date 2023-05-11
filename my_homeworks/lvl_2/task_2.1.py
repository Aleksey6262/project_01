# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# Решение
#задаем массив
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

def bubble (data):
  n = len(data)
  for i in range (n-1):
    for j in range (n-i-1):
      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
  return data

def minimum(arr):
    print ("МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
    print ("Метод сортировки пузырьком")
    for data in arr:
       print ("в массиве:", data, "min =", bubble(data)[0])

def maximum(arr):
    print ("МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
    print ("Метод сортировки пузырьком")
    for data in arr:
        print ("в массиве:", data, "max =", bubble(data)[len(data)-1])

def main():
 print (minimum(arr))
 print (maximum(arr))

print (main())




