rkr = int(input('Задайте радиус круга: '))
akv = int(input('Задайте сторону квадрата: '))
print (rkr, akv)
PI = 3.141562
Skr = PI * rkr ** 2
Skr = round(Skr, 2)
Lokr = 2 * PI* rkr
Lokr = round(Lokr, 2)
Pkv = 4 * akv
Skv = akv ** 2
print("Площадь круга", Skr)
print("Длина окружности", Lokr)
print("Периметр квадрата", Pkv)
print("Площадь круга", Skv)