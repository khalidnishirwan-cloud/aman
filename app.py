from flask import Flask, render_template, request, redirect, jsonify, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    if "user" not in session:
        return redirect('/login')
    return render_template('index.html', user=session["user"])

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email,password) VALUES (?,?)",(email,password))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email,password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = email
            return redirect('/')
        else:
            return "خطأ"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    msg = data.get("message")
    return jsonify({"response": "🤖 " + msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
