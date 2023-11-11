# Apiden alınan verileri SQL veritabanına kaydetmeye yarayan kod.
import requests
import sqlite3


api_url = "https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text"
response = requests.get(api_url)
data = response.text


cleaned_data = ''.join(e for e in data if e.isalnum() or e.isspace())


conn = sqlite3.connect('kelimeler.db')
cursor = conn.cursor()
words = cleaned_data.split()

cursor.execute('''CREATE TABLE IF NOT EXISTS kelimeler (
                  id INTEGER PRIMARY KEY,
                  kelime TEXT)''')

for word in words:
    cursor.execute("INSERT INTO kelimeler (kelime) VALUES (?)", (word,))
conn.commit()

conn.close()
