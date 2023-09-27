#код в котором может возникнуть исключение помещено в try
try:
#вводим четырехзначное число
num=input("Enter a four-digit number:")
#выводим на экран позиции четырехзначного числа с помощью индексов
print("The digit in the thousands position is",  num[0])
print("The number in the hundreds position is", num[1])
print("The digit in the tens position is", num[2])
print("The digit in the tens position is", num[3])
except ValueError:
print("Ввод данных неверный")
