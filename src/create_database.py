import sqlite3


# Create connection to SQLite database
connection = sqlite3.connect("database/world_cup.db")


print("Database created successfully!")


# Close connection
connection.close()