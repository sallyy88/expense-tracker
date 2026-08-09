import sqlite3

connection = sqlite3.connect("expenses.db") # db stands for database
# If expenses.db doesn't exist yet, it creates a brand new, empty database file with that name
# If expenses.db already exists, it just opens a connection to it
# Either way, what you get back is stored in connection — think of this as your program's link to that database file, 
# similar in spirit to how open("expenses.json", "r") gave you a connection to a file.

cursor = connection.cursor()
# Here's a useful analogy: if connection is like the phone line connecting you to the database, 
# the cursor is the actual telephone you use to talk through that line

# cursor.execute(...) is how u send any command to the database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT
    )
""")

while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Filter by category")
    print("4. Delete expense")
    print("5. Edit expense")
    print("6. Quit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date: ")

        # you need to use the ? place holders for security reasons
        # This matters for a real reason: if you insert user input directly into SQL text like that, 
        # it opens up a serious security vulnerability called SQL injection — where a malicious user could 
        # type something crafted to manipulate or damage your database.
        # Using ? placeholders lets the database safely handle the values separately from the command itself, avoiding that risk entirely.
        cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
        connection.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM expenses")
        results = cursor.fetchall()
        
        total = 0
        category_totals = {}
        
        for row in results:
            amount = row[1]
            category = row[2]
            
            # add `amount` to `total`
            total = total + amount
            
            # check if `category` is already in category_totals — if yes, add to it; if no, create it
            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount
            
            print(row[1], row[2], row[3])
        
        print(f"Total amount: {total}")
        print(f"Category totals: {category_totals}")

    elif choice == "3":
        filter_category = input("Enter category to filter by: ")

        # WHERE category = ? — meaning "only give me rows where the category column matches this value."
        # without the where category == ? it will give every row but with it,
        # it goes into each row and searches for the column with that category of the filter
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (filter_category,))
        results = cursor.fetchall()
        
        total = 0
        
        for row in results:
            # print each matching row, and add to a total
            print(row[1], row[2], row[3])
            total = total + row[1]

        
        print(f"Total for {filter_category}: {total}")


    elif choice == "4":
        cursor.execute("SELECT * FROM expenses")
        results = cursor.fetchall()
        
        for row in results:
            print(row[0], row[2], row[1])  # id, category, amount — helps user pick which one
        
        delete_id = int(input("Enter the id of the expense to delete: "))
        
        # write the DELETE execute() line here, using delete_id
        cursor.execute("DELETE FROM expenses WHERE id = ?", (delete_id,))
        
        connection.commit()

    elif choice == "5":
        cursor.execute("SELECT * FROM expenses")
        results = cursor.fetchall()
        
        for row in results:
            print(row[0], row[2], row[1])  # id, category, amount
        
        edit_id = int(input("Enter the id of the expense to edit: "))
        
        new_amount = float(input("Enter new amount: "))
        new_category = input("Enter new category: ")
        new_date = input("Enter new date: ")
        
        cursor.execute("UPDATE expenses SET amount = ?, category = ?, date = ? WHERE id = ?", (new_amount, new_category, new_date, edit_id))
        connection.commit()
        
    elif choice == "6":
        break

    else:
        print("Invalid choice.")


