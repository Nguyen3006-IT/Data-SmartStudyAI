from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
#----------------------------------------Home-----------------------------------
@app.route("/")
def home():
  return """API SAVE Message"""
#------------------------------------Post_Method-----------------------------------
@app.route("/save", methods=["POST"])
def savemid():
  data = request.get_json()
  try:
    if "message" in data:
      time = data["timestamp"] //1000
      id = data["mid"]
      message = data["message"]
      saveMid(time=time, message=message, id=id)
      return jsonify({"message": "Save mid Successfully"})
      
    else: 
      return jsonify({"message": "Erorr"}), 400

  except Exception as e:
    print(e), 500
#------------------------------------get_Method-----------------------------------
@app.route("/get_message", methods=["GET"])
def getmid():
  message_id = request.args.get("id")
  dic_msg = {
    "message_id": message_id,
    "message_text": getMid(msg_id=message_id)
  }
  return jsonify(dic_msg)

#------------------------------------Module-----------------------------------
#sql_cmd
sql_cmd = """
SELECT * FROM {} WHERE {}=?
"""#(format) table -> name_table

def saveMid(time, message, id):
  from re import search
  if not search("^https://scontent.xx.fbcdn.net/v.+", message):
    connection = sqlite3.connect("data_message.db", check_same_thread=False)
    cursor = connection.cursor()
    try:
      cursor = connection.cursor()
      cursor.execute("""
        CREATE TABLE Data_Message (
          TimeStamp INTEGER, 
          Message_ID TEXT,
          Message_Text TEXT);
        """)
    except:
      pass
    cursor.execute(sql_cmd.format("Data_Message", "Message_Text"), (message,))
    if not cursor.fetchone():
      cursor.execute("INSERT INTO Data_Message VALUES (?, ?, ?)", (time, id, message))
      connection.commit()
    connection.close()
    delete_data_expires("data_message.db", "Data_Message")
  
  else:
    conn = sqlite3.connect("data_image.db", check_same_thread=False)
    cursor = conn.cursor()
    try:
      cursor = conn.cursor()
      cursor.execute("""
        CREATE TABLE Data_Image (
          TimeStamp INTEGER, 
          Message_ID TEXT,
          Url_Image TEXT);
        """)
    except:
      pass

    cursor.execute("INSERT INTO Data_Image VALUES (?, ?, ?)", (time, id, message))
    conn.commit()  
    conn.close()
    
    delete_data_expires("data_image.db", "Data_Image")


def getMid(msg_id):
  connect = sqlite3.connect("data_message.db", check_same_thread=False)
  cur = connect.cursor()
  cur.execute(sql_cmd.format("Data_Message", "Message_ID"), (msg_id,))
  result = cur.fetchone()[-1]
  
  if not result: # lấy ảnh
    connect = sqlite3.connect("data_image.db", check_same_thread=False)
    cur = connect.cursor()
    cur.execute(sql_cmd.format("Data_Image", "Message_ID"), (msg_id,))
    return cur.fetchone()[-1]
  
  return result


def delete_data_expires(file_name, table):
  try:
    TimeStamp_Now = int(datetime.now().timestamp())
    connection = sqlite3.connect(file_name, check_same_thread=False)
    cur = connection.cursor()
    cur.execute(f"DELETE FROM {table} WHERE TimeStamp < {TimeStamp_Now-260000}")
    connection.commit()
    connection.close()
  except Exception as e:
    print(e)
  
#run
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)

