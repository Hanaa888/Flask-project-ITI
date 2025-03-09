from flask import Flask, request,render_template
import sqlite3

DATABASE = "patients.db"

app = Flask(__name__)

def connect():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn  

def patient(_id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserInfo WHERE ID = ?", (_id,))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        _id = request.form.get('_id')  
        if _id is None or not _id.isdigit():
            return "Invalid ID"

        user = patient(int(_id))
        if user:
            return render_template('patients.html', user=user)
        else:
            return render_template('not.html', user=user)
    return render_template('patients.html')
    

if __name__ == "__main__":
    app.run(port=3000, debug=True , host='0.0.0.0')
