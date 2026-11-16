from flask import Flask, render_template, request, jsonify
import requests
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('homio.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS family_members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT NOT NULL,
        assistant_reply TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

init_db()

def save_chat(user_msg, reply):
    conn = sqlite3.connect('homio.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO chats (user_message, assistant_reply) VALUES (?, ?)', (user_msg, reply))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    try:
        response = requests.post('http://localhost:11434/api/generate', json={
            "model": "homio:latest",
            "prompt": user_msg,
            "stream": False
        }, timeout=60)
        reply = response.json().get('response', 'Mujhe samajh nahi aaya.')
    except Exception as e:
        reply = "Ollama chal nahi raha hai, pehle Ollama on karo. Error: " + str(e)

    save_chat(user_msg, reply)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)