#код в котором может возникнуть исключение помещено в try
try:
#вводим кол-во школьников и мандаринов
n=int(input("Количество школьников"))
k=int(input("Количество мандаринов"))
#вычисление кол-во мандаринов для каждого школьника
whole_tan=k//n
#вычисление оставшиееся кол-во мндаринов в корзине
remain_basket=k-(whole_tan*n)
#вывод c использованием f-строки
print(f"Количество мандаринов для каждого школьника: {whole_tan} \n Количество мандаринов оставшееся в корзине: {remain_basket} ")
except ValueError:
    print("Ввод данных неверный")
