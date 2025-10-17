from Library import EBook, PrintedBook

def test_late_fee():
    ebook = EBook("Test", "Author", 10)
    printed = PrintedBook("Test2", "Author2", 15)

    # Simple checks to verify polymorphism
    assert ebook.calculate_late_fee(2) == 1.0
    assert printed.calculate_late_fee(2) == 4
