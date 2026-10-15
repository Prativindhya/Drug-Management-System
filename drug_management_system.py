import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="drug_db",
    charset="utf8"
)
cursor = db.cursor()


def add_drug():
    drug_id = input("Enter unique drug ID: ")
    name = input("Enter drug name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    expiry = input("Enter expiry (YYYY-MM-DD): ")
    cursor.execute(
        "INSERT INTO drugs (id, name, quantity, price, expiry) VALUES (%s, %s, %s, %s, %s)",
        (drug_id, name, quantity, price, expiry)
    )
    db.commit()
    print("Drug added successfully.\n")


def view_all():
    cursor.execute("SELECT * FROM drugs")
    rows = cursor.fetchall()
    print("\nDrug List:")
    print("ID | Name | Quantity | Price | Expiry ")
    for i in rows:
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")


def update_drug():
    drug_id = input("Enter drug ID to update: ")
    print("Update:\n1. Name\n2. Quantity\n3. Price\n4. Expiry ")
    choice = input("Enter option: ")
    if choice == '1':
        value = input("New name: ")
        cursor.execute("UPDATE drugs SET name = %s WHERE id = %s", (value, drug_id))
    elif choice == '2':
        value = input("New quantity: ")
        cursor.execute("UPDATE drugs SET quantity = %s WHERE id = %s", (value, drug_id))
    elif choice == '3':
        value = input("New price: ")
        cursor.execute("UPDATE drugs SET price = %s WHERE id = %s", (value, drug_id))
    elif choice == '4':
        value = input("New expiry date (YYYY-MM-DD): ")
        cursor.execute("UPDATE drugs SET expiry = %s WHERE id = %s", (value, drug_id))
    else:
        print("Invalid choice.")
        return
    db.commit()
    print("Drug updated successfully.\n")


def delete_drug():
    drug_id = input("Enter drug ID to delete: ")
    cursor.execute("DELETE FROM drugs WHERE id = %s", (drug_id,))
    db.commit()
    print("Drug deleted successfully.\n")


def search_drug():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM drugs WHERE name LIKE %s", ('%' + name + '%',))
    rows = cursor.fetchall()
    print("Search Results:")
    for i in rows:
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")


def menu():
    while True:
        print("\nDrug Management System")
        print("1. Add Drug")
        print("2. View All Drugs")
        print("3. Update Drug")
        print("4. Delete Drug")
        print("5. Search Drug")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_drug()
        elif choice == '2':
            view_all()
        elif choice == '3':
            update_drug()
        elif choice == '4':
            delete_drug()
        elif choice == '5':
            search_drug()
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Invalid option.")


menu()
cursor.close()
db.close()
