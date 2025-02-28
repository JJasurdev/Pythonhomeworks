import sqlite3

# Step 1: Create SQLite Database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Step 2: Create Roster Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Step 3: Insert Data
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

conn.commit()

# Step 4: Update Data (Change Jadzia Dax to Ezri Dax)
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

conn.commit()

# Step 5: Query Data (Retrieve Name and Age of Bajoran characters)
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Step 6: Delete Data (Remove characters aged over 100 years)
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")

conn.commit()

# Step 7: Add New Column 'Rank'
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# Step 8: Update Data with Rank Information
cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

conn.commit()

# Step 9: Advanced Query (Retrieve all characters sorted by Age in descending order)
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
sorted_characters = cursor.fetchall()
print("Characters sorted by Age:", sorted_characters)

# Close the connection
conn.close()
