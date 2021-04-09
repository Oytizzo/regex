# This is for writing csv
import csv

# --------------------------csv from lists---------------------------
field_names = ["Name", "Author", "Published", "Price", "Category"]
book1 = ["Computer Programming Part 1", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "240.00", "Programming"]
book2 = ["Computer Programming Part 2", "Tamim Shahriar Subeen", "Dimik Prokashoni", "250.00", "Programming"]
book3 = ["Learn Programming with Python", "Tamim Shahriar Subeen", "Dimik Prokashoni", "200.00", "Programming"]

book_list = [book1, book2, book3]

with open("books.csv", "w") as csvf:
    csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    for book in book_list:
        csv_writer.writerow(book)

# ----------------------csv from dictionary-------------------------
field_names = ["Name", "Author", "Publisher", "Price"]
book1 = {
    "Name": "Computer Programming, Part 1",
    "Author": "Tamim Shahriar Subeen",
    "Publisher": "Onnorokom Prokashoni",
    "Price": "240.00"
}
book2 = {
    "Name": "Computer Programming, Part 2",
    "Author": "Tamim Shahriar Subeen",
    "Publisher": "Dimik Prokashoni",
    "Price": "240.00"
}
book3 = {
    "Name": "Learn Programming with Python",
    "Author": "Tamim Shahriar Subeen",
    "Publisher": "Dimik Prokashoni",
    "Price": "200.00"
}

book_list = [book1, book2, book3]

with open("book_list.csv", "w") as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)
