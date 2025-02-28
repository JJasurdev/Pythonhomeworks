import sqlite3

# Step 1: Create SQLite Database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 2: Create Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Step 3: Insert Data
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

conn.commit()

# Step 4: Update Data (Change Year_Published of 1984 to 1950)
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

conn.commit()

# Step 5: Query Data (Retrieve Title and Author of Dystopian books)
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
dystopian_books = cursor.fetchall()
print("Dystopian Books:", dystopian_books)

# Step 6: Delete Data (Remove books published before 1950)
cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

conn.commit()

# Step 7: Add New Column 'Rating'
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")

# Step 8: Update Data with Rating Information
cursor.executemany("""
UPDATE Books SET Rating = ? WHERE Title = ?
""", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])

conn.commit()

# Step 9: Advanced Query (Retrieve all books sorted by Year_Published in ascending order)
cursor.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
""")
sorted_books = cursor.fetchall()
print("Books sorted by Year_Published:", sorted_books)

# Close the connection
conn.close()
