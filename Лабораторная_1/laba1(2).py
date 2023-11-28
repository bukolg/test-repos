#Лаба_1 (2 задание)
# Определить количество книг на дискете
V_simbol = 4
n_simbol = 25
n_Line = 50
n_page = 100
v_disk = 1.44
volume_disk = v_disk * 1024 ** 2
voluve_book = V_simbol * n_simbol * n_Line * n_page
print(volume_disk, voluve_book)

n = int(volume_disk / voluve_book)

print(f"Количество книг, помещающихся на дискету, = {n}")