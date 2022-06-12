import copy
from itertools import cycle
import re
import sys
from unittest import result

#возведение в степень
def pow_matrix(matrix, deg):
    for i in range(deg+1):
        matrix[i][i] = 1

    old_m = copy.deepcopy(matrix)
    new_m = []

    s = 0
    
    t = []
    #произведение матриц находится по стандартным правилам умножения матриц
    for d in range(1, deg):
        for x in range(0, deg + 1):
            for y in range(0, deg + 1):
                for i in range(0, deg + 1):
                    s = s + matrix[x][i] * old_m[i][y]
                    s = 1 if s > 0 else 0
                t.append(s)
                s = 0
            new_m.append(t)
            t = []
        if new_m == old_m:
            return old_m

        old_m = copy.deepcopy(new_m)
        new_m = []

        
    return old_m

#функиция чтения матрицы
def read_matrix():
    f = open("matrix.txt", "r") #отрытие файл
    s = []
    s.append([int(x) for x in f.readline().split(",")])
    number_of_vertex =len(s[0]) #количество вершин
    f.seek(0)
    matrix = []
    #создание мтрицы смежности
    ways = f.readlines()
    for i in range(0, number_of_vertex - 1):
        ways[i] = ways[i][: -1]

    for i in range(number_of_vertex):
        matrix.append([int(x) for x in ways[i].split(", ")])

    return (matrix, number_of_vertex - 1)

#находим одинаковые строки в матрице
def get_cycles(result_matrix):
    cycles = []
    t = []
    used_lines = []

    for i in range(0, len(result_matrix)):
        for j in range(i, len(result_matrix)):
            if (i != j) & (result_matrix[i] == result_matrix[j]):
                if i not in t:
                    t.append(i)
                if j not in t:
                    t.append(j)
        if result_matrix[i] not in used_lines:
            used_lines.append(result_matrix[i])
            cycles.append(t)
            t = []


    if len(cycles) == 0:
        print("Циклов нет")
    else:
        print("Множества вершин:")
        print_uniq_cycles(cycles)

#вывод множеств
def print_uniq_cycles(cycles):
    for row in range(len(cycles)):
        for column in range(len(cycles[row])):
            sys.stdout.write(chr(cycles[row][column] + 65) + " ")
        print("")


#функция main
def main():
    (matrix, deg) = read_matrix() #запускаем функцию считывания матрицы
    result_matrix = pow_matrix(matrix, deg) #возводим матрицу в степень 
    get_cycles(result_matrix) #ищем одинаковые строки 
    input()


main()