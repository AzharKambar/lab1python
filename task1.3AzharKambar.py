#код в котором может возникнуть исключение помещено в try
try:
 #ввод переменной
a=int(input())
#вывод трех последовательных чисел в отдельном списке
print(a,a+1,a+2,sep='\n')
except ValueError :
print("Ввод данных неверный")
