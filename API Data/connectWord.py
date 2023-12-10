import sqlite3

class Matching:
  def __init__(self) -> None:
    self.connection = sqlite3.connect("connect_word_Vie.db")
    self.cur = self.connection.cursor()
  
  def VieFirst(self, text:str) -> tuple[str]:
    self.cur.execute(
      f"""
      SELECT * FROM words WHERE word LIKE '{text}%'
      ORDER BY RANDOM() LIMIT 1; 
      """)
    return self.cur.fetchone()
  
  def VieLast(self, text:str) -> tuple[str]:
    self.cur.execute(
      f"""
      SELECT * FROM words WHERE word LIKE '%{text}'
      ORDER BY RANDOM() LIMIT 1; 
      """)
    return self.cur.fetchone()

  
#-------------------------------add data-------------------------------#
  def addWord(self, word) -> dict:
    try:
      if len(word) == 2:
        self.cur.execute("INSERT INTO words (word) VALUES (?);", (word,))
        self.connection.commit()
      return {"message": "Save Success"}
    except:
      return {"message": "Error"}

  def addAllWords(self, data:list[tuple]) -> dict:
    try:
      for word in data:
        if len(word[0].split()) != 2:
          data.remove(word)
          
      self.cur.executemany("INSERT INTO words (word) VALUES (?);", data)
      self.connection.commit()
      return {"message": "Save Success"}
    except:
      return {"message": "Error"}