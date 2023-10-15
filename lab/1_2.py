volume_of_disk = 1.44 * 2**10 * 2**10 #объем диска в байтах
pages = 100
lines = 50
symbols = 25
symbol_weight = 4
volume = pages * lines * symbols * symbol_weight
count_of_books = int(volume_of_disk // volume)

print("Количество книг, помещающихся на дискету:", count_of_books)
