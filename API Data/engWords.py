import sqlite3, re

def find_word(word:str):
  word = re.sub('\([^)]*\)|[\W]', ' ', word)
  word = re.sub('\s+', ' ', word)
  
  connection = sqlite3.connect("Vocabulary.db", check_same_thread=False)
  cur = connection.cursor()
  
  dataDB = cur.execute("SELECT * FROM vocabulary WHERE word=?", (word,))
  data = dataDB.fetchone()
  
  if data:
    return {
      "word": data[0],
      "meaning": data[1]
    }
  
  return 

