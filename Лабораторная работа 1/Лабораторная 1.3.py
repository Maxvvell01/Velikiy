disk_size_in_mb = 1.44
number_of_pages_in_book = 100
number_of_str_on_page = 50
number_of_symbols_in_str = 25
bytes_for_symbol = 4

disk_size_in_byte = disk_size_in_mb * 1024 * 1024

bytes_for_book = number_of_pages_in_book * number_of_str_on_page * number_of_symbols_in_str * bytes_for_symbol

amount_of_books_on_disk = round(disk_size_in_byte // bytes_for_book,)

print("Количество книг, помещающихся на дискету:", amount_of_books_on_disk)
