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

def selectFirst(charFirst:str):
    connection = sqlite3.connect("Vocabulary.db", check_same_thread=False)
    cur = connection.cursor()
    
    #tìm tất cả các từ khi chỉ có chữ cái đầu 
    dataDB = cur.execute(
        f"""
        SELECT * FROM Vocabulary WHERE word LIKE '{charFirst}%' AND word NOT LIKE '% %'
        ORDER BY RANDOM() LIMIT 1;
        """
    )

    data = dataDB.fetchone()

    return data if data else None


def selectLast(charOut:str):
    connection = sqlite3.connect("Vocabulary.db", check_same_thread=False)
    cur = connection.cursor()
    
    #tìm tất cả các từ khi chỉ có chữ cái đầu 
    dataDB = cur.execute(
        f"""
        SELECT * FROM Vocabulary WHERE word LIKE '%{charOut}' AND word NOT LIKE '% %'
        ORDER BY RANDOM() LIMIT 1;
        """
    )

    data = dataDB.fetchone()

    return data if data else None
