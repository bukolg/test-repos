#Поиск индекса элемента в списке товаров
# написать функцию для поиска индекса первого вхождения элемента в список товаров
def search_item(lis, item):
    if item in lis:
        return lis.index(item)
    else:
        return None

list_item = ["гель", "лосьен", "крем", "шампунь", "гель", "крем", "спрей"]
print(f"Список товаров: {list_item}")

for item_search in ["крем", "гель", "порошок", "лосьен"]:
    item_index = search_item(list_item, item_search)
    if item_index is not None:
        print(f"Первое вхождение товара '{item_search}' имеет индекс {item_index}.")
    else:
        print(f"Товара '{item_search}' нет в списке (None)")
