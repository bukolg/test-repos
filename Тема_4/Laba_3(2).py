#написать функцию, принимающую две строки, в которых перечислены участники без пробелов
def find_common_participants(list1, list2):
    return list(set(list1) & set(list2))

grupp1 = input("Введите без пробелов через запятую первую группу участников:")
grupp2 = input("Введите без пробелов через запятую вторую группу участников:")

grupp1_split = grupp1.split(',')
grupp2_split = grupp2.split(',')

print("Первая группа участников:", grupp1_split)
print("Вторая группа участников:", grupp2_split)

common_grupp = find_common_participants(grupp1_split, grupp2_split)

print("Общие участники до сортировки:", common_grupp)

common_grupp.sort()
print("Общие участники после сортировки:", common_grupp)
