#Частотный анализ букв в тексте
def count_letters(text):
    dictionary = {}  # Создаем пустой словарь, определяющий буквы и их количество в тексте
    lowercase = text.lower()  # преобразуем символы строки в нижний регистр
    print(f"Текст в нижнем регистре: {lowercase}")

    for symbol in lowercase:
        if symbol.isalpha():  # Проверка символов на букву в нижнем регистре
            if symbol in dictionary:
                dictionary[symbol] += 1
            else:
                dictionary[symbol] = 1
    return dictionary
def calculate_frequency(dictionary):
    total_number = sum(dictionary.values())
    frequencies = {} #Создаем пустой словарь, где буква используется как ключ, а ее частота как значение

    for letter, count in dictionary.items():
        frequency = round(count / total_number, 2) # Вычисляем частоту каждой буквы, округлив до двух знаков после запятой
        frequencies[letter] = frequency  # Заполняем словарь поэлементно
    return frequencies


text = input("Введите любой текст:")
letters = count_letters(text)
frequencies = calculate_frequency(letters)


for letter, freq in frequencies.items():
    print(f"{letter}: {freq}")  #Печать в столбик словаря с частотами
