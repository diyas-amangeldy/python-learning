"""items = ["A", "B", "C", "D", "E", "F", "G"]

Напиши:
def paginate(items, page, page_size):
    ...
Функция должна вернуть элементы только указанной страницы.
Например:

paginate(items, 1, 3)
# ["A", "B", "C"]

paginate(items, 2, 3)
# ["D", "E", "F"]

paginate(items, 3, 3)
# ["G"]"""


"""
items = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y",
    "Z"
]
def paginate(items, page_num, page_size):
    book = []
    page = []
    pages=(int(len(items)/page_size))
    for_last_page = len(items)%page_size
    count = 0
    for i in range(pages):
        for element in range(page_size):
            page.append(items[count])
            count += 1
        book.append(page)
        page = []
    for i in range(for_last_page):
        page.append(items[count])
        count += 1
    book.append(page)
    print(book[page_num-1])
paginate(items, 3, 10)
"""
items = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y",
    "Z"
]
def paginate(items, page_num, page_size):
    start_index=(page_num-1)*page_size
    end_index=start_index+page_size
    return items[start_index:end_index]
print(paginate(items,3,10))