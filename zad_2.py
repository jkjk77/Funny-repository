import math
import statistics as stat
from datetime import datetime


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return "Miasto: {}\nUlica: {}\nKod pocztowy: {}\nGodziny otwarcia: {}\nTelefon: {}".format(
            self.city, self.street, self.zip_code, self.open_hours, self.phone
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return "Imię: {}\nNazwisko: {}\nData zatrudnienia: {}\nData urodzenia: {}\nMiasto: {}\nUlica: {}\nKod pocztowy: {}\nTelefon: {}".format(
            self.first_name,
            self.last_name,
            self.hire_date,
            self.birth_date,
            self.city,
            self.street,
            self.zip_code,
            self.phone,
        )


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Biblioteka: {}\nData publikacji: {}\nAutor: {}\nIlość stron: {}".format(
            self.library.city,
            self.publication_date,
            self.author_name,
            self.number_of_pages,
        )


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return "Pracownik: {}\nStudent: {}\nKsiążki: {}\nData zamówienia: {}".format(
            self.employee,
            self.student,
            [str(book) for book in self.books],
            self.order_date,
        )


library_1 = Library(
    "Katowice",
    "Ul. Adamskiego 5",
    "22-222",
    "Poniedziałek 8-18\nWtorek 8-18\nŚroda 8-18\nCzwartek 10-20\nPiątek 8-18\nSobota 8-13",
    "111222333",
)
library_2 = Library(
    "Ruda Śląska",
    "Ul. Chryzantem 11",
    "33-333",
    "Poniedziałek 8-17\nWtorek 8-17\nŚroda 8-17\nCzwartek 10-20\nPiątek 8-17\nSobota 8-13",
    "111222333",
)

book_1 = Book(library_1, datetime(2020, 1, 1), "Piotr", "Matuszak", 69)
book_2 = Book(library_2, datetime(2020, 5, 5), "Miotr", "Patuszak", 79)
book_3 = Book(library_1, datetime(2018, 4, 9), "Rafał", "Kwiatek", 150)
book_4 = Book(library_2, datetime(2017, 10, 10), "Raphael", "Flower", 99)
book_5 = Book(library_2, datetime(2021, 11, 7), "Michał", "Matuszak", 17)

employee_1 = Employee(
    "Jakub",
    "Kęstowicz",
    datetime(2015, 8, 16),
    datetime(2001, 2, 24),
    "Ruda Śląska",
    "Chryzantem",
    "41-710",
    "555444442",
)
employee_2 = Employee(
    "Machał",
    "Mituszak",
    datetime(2015, 8, 20),
    datetime(1998, 1, 1),
    "Katowice",
    "Bogucicka",
    "41-800",
    "222333444",
)
employee_3 = Employee(
    "Jan",
    "Nowak",
    datetime(2016, 7, 10),
    datetime(1980, 5, 5),
    "Hożuf",
    "Cicha",
    "55-555",
    "333333999",
)

order_1 = Order(employee_1, "Jerzy Kowal", [book_2, book_3], datetime(2022, 10, 17))
order_2 = Order(employee_2, "Jan Wisniewski", [book_1], datetime(2022, 5, 5))

print(str(order_1))
print(str(order_2))
