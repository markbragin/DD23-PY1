data_size_mb = 1.44
bytes_in_mb = 2**20
pages = 100
lines = 50
chars = 25
bytes_in_char = 4

books = round(
    data_size_mb * bytes_in_mb // (pages * lines * chars * bytes_in_char)
)

print("Количество книг, помещающихся на дискету:", books)

