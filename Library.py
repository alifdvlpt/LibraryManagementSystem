# Library Management System
# Part B – Advance Programming Assignment

from abc import ABC, abstractmethod


# -------------------------------
# Base Class (Encapsulation + Abstraction)
# -------------------------------
class Book:
    def __init__(self, title, author, price):
        self.__title = title       # private attribute
        self.__author = author     # private attribute
        self.__price = price       # private attribute

    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}, Price: ${self.__price}")

    def calculate_late_fee(self, days_late):
        """Default method (can be overridden by subclasses)"""
        return days_late * 1


# -------------------------------
# Inheritance + Polymorphism
# -------------------------------
class EBook(Book):
    def calculate_late_fee(self, days_late):
        return days_late * 0.5  # lower fee for eBooks


class PrintedBook(Book):
    def calculate_late_fee(self, days_late):
        return days_late * 2  # higher fee for printed books


# -------------------------------
# SOLID Principle: Interface Segregation + Dependency Inversion
# -------------------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using your Credit Card.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} in Cash.")


# -------------------------------
# Library Management System Runner
# -------------------------------
if __name__ == "__main__":
    # Create book objects
    ebook = EBook("Digital Fortress", "Dan Brown", 10)
    printed = PrintedBook("Harry Potter", "J.K. Rowling", 15)

    # Display info
    print("=== Book Details ===")
    ebook.display_info()
    printed.display_info()

    # Show late fees
    print("\n=== Late Fees ===")
    print("EBook Late Fee (3 days):", ebook.calculate_late_fee(3))
    print("Printed Book Late Fee (3 days):", printed.calculate_late_fee(3))

    # Payment demonstration (Dependency Injection)
    print("\n=== Payment ===")
    payment_method = CreditCardPayment()   # could switch to CashPayment() easily
    total_amount = ebook.calculate_late_fee(3) + printed.calculate_late_fee(3)
    payment_method.pay(total_amount)

    print("\nProgram finished successfully!")
