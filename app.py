from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# إنشاء قاعدة البيانات
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ✅ الصفحة الرئيسية (مباشرة بدون تحويل)
@app.route('/')
def index():
    return render_template('index.html')

# تسجيل
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            conn.close()
            return redirect('/')
        except:
            return "الإيميل مستخدم"

    return render_template('register.html')

# تسجيل دخول (اختياري)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# API
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message')
    return jsonify({"response": f"🤖: {message}"})
