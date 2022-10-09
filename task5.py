#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
#Пример двух заданных многочленов:
#23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#Результат:
#40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from task4 import createEquation

def readEquation():
    firstEquation = createEquation()
    equation = {}

    firstEquation = firstEquation.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]

    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace('+', '').split('x^')
        equation[int(firstEquation[i][1])] = int(firstEquation[i][0])
    return equation

finalWord = {}
word1 = readEquation()
word2 = readEquation()
print(word1)
print(word2)

for i in range (max(len(word1), len(word2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)

print(finalWord)