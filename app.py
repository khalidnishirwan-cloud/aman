from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os  # مهم لتشغيل السيرفر على أي منصة

app = Flask(__name__)

# إنشاء قاعدة البيانات تلقائيًا
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

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة تسجيل حساب جديد
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
            return redirect('/login')
        except sqlite3.IntegrityError:
            return "هذا الإيميل مستخدم بالفعل"

    return render_template('register.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            return redirect('/')
        else:
            return "بيانات غير صحيحة"

    return render_template('login.html')

# واجهة الدردشة التجريبية
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message')
    # الآن مجرد رد تجريبي، لاحقًا نربطه بـ OpenAI
    return jsonify({"response": f"🤖: {message}"})

# تشغيل السيرفر
if __name__ == '__main__':
    # مهم جدًا للسيرفرات السحابية مثل Railway
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
