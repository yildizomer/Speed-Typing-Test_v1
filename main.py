# Ömer Faruk Yıldız

import sqlite3
import random
import time


conn = sqlite3.connect("kelimeler.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS kullanıcılar (
                  kullanıcı_adı TEXT PRIMARY KEY,
                  en_yüksek_skor INTEGER)''')
conn.commit()
cursor.execute("SELECT kelime FROM kelimeler")
words = [row[0] for row in cursor.fetchall()]


user_name = input("Kullanıcı adınızı girin: ")
user_scores = []
cursor.execute("SELECT en_yüksek_skor FROM kullanıcılar WHERE kullanıcı_adı = ?", (user_name,))
result = cursor.fetchone()
if result is not None:
    highest_score = result[0]
else:
    highest_score = 0


game_duration = 60

while True:
    input("Oyuna başlamak için ENTER tuşuna basın...")

    start_time = time.time()
    end_time = start_time + game_duration
    current_game_score = 0

    while time.time() < end_time:
        target_word = random.choice(words)
        user_input = input(target_word + ": ")

        if user_input.strip() == target_word:
            current_game_score += 5
        else:
            print("Yanlış kelime! Puan kazanamazsınız.")

    user_scores.append(current_game_score)  

    highest_score = max(highest_score, current_game_score)  

    cursor.execute("INSERT OR REPLACE INTO kullanıcılar (kullanıcı_adı, en_yüksek_skor) VALUES (?, ?)", (user_name, highest_score))
    conn.commit()

    print(f"Oyun Skoru: {current_game_score}")
    print(f"En Yüksek Skor: {highest_score}")

    play_again = input("Tekrar oynamak ister misiniz? (Evet/Hayır): ")
    if play_again.lower() != "evet":
        break


conn.close()
