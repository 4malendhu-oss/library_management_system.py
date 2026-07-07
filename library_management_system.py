library = {}

while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Search Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library[book] = "Available"
        print("Book added successfully!")

    elif choice == "2":
        if library:
            print("\nBooks:")
            for book, status in library.items():
                print(f"{book} : {status}")
        else:
            print("No books available.")

    elif choice == "3":
        book = input("Enter book name: ")
        if book in library:
            if library[book] == "Available":
                library[book] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter book name: ")
        if book in library:
            library[book] = "Available"
            print("Book returned successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        book = input("Enter book name to delete: ")
        if book in library:
            del library[book]
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "6":
        book = input("Enter book name to search: ")
        if book in library:
            print(f"{book} : {library[book]}")
        else:
            print("Book not found.")

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")