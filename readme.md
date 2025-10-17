# Library Management System

## Overview
This is a **Library Management System** implemented in Python. The system demonstrates key **object-oriented programming (OOP)** concepts including **encapsulation, abstraction, inheritance, polymorphism**, and **SOLID principles**. It supports different types of books (printed and electronic) and allows simulation of late fee calculation and payment processing.

---

## Features
- **Book Management**:
  - Store book details: title, author, and price.
  - Display book information.
  - Calculate late fees (differentiated for printed and eBooks).

- **OOP Concepts**:
  - **Encapsulation**: Book details are private.
  - **Abstraction**: Abstract class for payment methods.
  - **Inheritance & Polymorphism**: Different types of books have custom late fee calculation.

- **Payment System**:
  - Supports multiple payment methods using **Interface Segregation and Dependency Inversion**.
  - Built-in examples: `CreditCardPayment` and `CashPayment`.
  - Easy to extend for new payment types.

- **Late Fee Calculation**:
  - Printed books: $2/day
  - eBooks: $0.5/day
  - Default fee for general books: $1/day

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/alifdvlpt/LibraryManagementSystem.git
   ```
2. Navigate to the project folder:
   ```bash
   cd LibraryManagementSystem
   ```
3. Run the Python program:
   ```bash
   python library_system.py
   ```

---

## Usage
1. **Create book objects**:
   ```python
   ebook = EBook("Digital . Fortress", "Dan Brown", 10)
   printed = PrintedBook("Harry Potter", "J.K. Rowling", 15)
   ```

2. **Display book details**:
   ```python
   ebook.display_info()
   printed.display_info()
   ```

3. **Calculate late fees**:
   ```python
   ebook.calculate_late_fee(3)      # 3 days late
   printed.calculate_late_fee(3)
   ```

4. **Make payments**:
   ```python
   payment_method = CreditCardPayment()
   total_amount = ebook.calculate_late_fee(3) + printed.calculate_late_fee(3)
   payment_method.pay(total_amount)
   ```

---

## Design Principles Demonstrated
- **Encapsulation**: Private attributes for book details.
- **Abstraction**: `Payment` abstract class defines a common interface for all payment types.
- **Inheritance & Polymorphism**: `EBook` and `PrintedBook` inherit from `Book` and override late fee calculation.
- **SOLID Principles**:
  - Interface Segregation: Different payment types implement only what they need.
  - Dependency Inversion: High-level modules depend on abstractions, not concrete implementations.

---

## GitHub Repository
You can find the full source code on GitHub: [https://github.com/alifdvlpt/LibraryManagementSystem](https://github.com/alifdvlpt/LibraryManagementSystem)

---

## License
This project is licensed under the MIT License.

