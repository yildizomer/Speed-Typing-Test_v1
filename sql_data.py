# Sql datasında istenilmeyen verilen silinmesi

import sqlite3


conn = sqlite3.connect('kelimeler.db')
cursor = conn.cursor()


silinecek_harfler = '.,-'  


sorgu = f"UPDATE kelimeler SET kelime = REPLACE(kelime, '{silinecek_harfler}', '')"


cursor.execute(sorgu)


conn.commit()


conn.close()
