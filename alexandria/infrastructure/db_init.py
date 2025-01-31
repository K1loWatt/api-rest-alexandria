import psycopg2

connection = psycopg2.connect(
    dbname='your_database_name',
    user='your_user',
    password='your_password',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS book_author (
    author_id INT,
    book_id INT,
    PRIMARY KEY (author_id, book_id),
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
)
''')

connection.commit()
cursor.close()
connection.close()
