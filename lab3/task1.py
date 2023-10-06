# def find_index(goods: list[str], target_good: str) -> int | None:
#     for i in range(len(goods)):
#         if goods[i] == target_good:
#             return i
#     return None


def find_index(goods: list[str], target_good: str) -> int | None:
    for i, good in enumerate(goods):
        if good == target_good:
            return i
    return None


items_list = ["яблоко", "банан", "апельсин", "груша", "киви", "банан"]

for find_item in ["банан", "груша", "персик"]:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(
            f"Первое вхождение товара '{find_item}' имеет индекс {index_item}."
        )
    else:
        print(f"Товар '{find_item}' не найден в списке.")
