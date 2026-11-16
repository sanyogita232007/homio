import sqlite3

# Database connect karo, nahi hai to ban jayegi
conn = sqlite3.connect('homio.db')
cursor = conn.cursor()

# Table 1 - Family Members
cursor.execute('''
CREATE TABLE IF NOT EXISTS family_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Table 2 - Chats
cursor.execute('''
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT NOT NULL,
    assistant_reply TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("Ho gaya! homio.db ban gayi aur dono tables ban gaye!")