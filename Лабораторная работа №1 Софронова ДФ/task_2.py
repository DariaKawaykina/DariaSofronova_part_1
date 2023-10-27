# TODO Найдите количество книг, которое можно разместить на дискете
ONE_SYMBOL = 4  # объем одного символа 4 байта
MEMORY = 1.44  # объем памяти дискеты в Мбайтах
memory_line = ONE_SYMBOL * 25  # объем памяти для 1 строки в байтах
memory_page = memory_line * 50  # объем памяти для 1 страницы в байтах
memory_book = (memory_page * 100) / 1024 / 1024 # объем памяти для 1 книги в Мбайтах
number_of_books = MEMORY / memory_book
print("Количество книг, помещающихся на дискету:", int(number_of_books // 1))
