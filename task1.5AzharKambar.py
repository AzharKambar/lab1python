#ввод длины ребра
edgelength=int(input('Введите длину ребра куба'))
#рассчет объема куба
volume=edgelength**3
#рассчет площади поверхности куба
area=6*edgelength**2
#вывод на экран значения объема и площади с использованием f-строки
print(f"Volume= {volume} \n Total surface area = {area}")