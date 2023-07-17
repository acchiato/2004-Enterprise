from flask import Flask, render_template, jsonify,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', students=students)

@app.route('/api/add_student', methods=['POST'])
def add_student():
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    student_id = request.form['student_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    amount_due = request.form['amount_due']

    cursor.execute("INSERT INTO student (student_id, first_name, last_name, dob, amount_due) VALUES (?, ?, ?, ?, ?)",
                   (student_id, first_name, last_name, dob, amount_due))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(message='Student added successfully')

@app.route('/api/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(message='Student deleted successfully')

@app.route('/api/update_student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    updated_data = request.get_json()
    first_name = updated_data.get('first_name')
    last_name = updated_data.get('last_name')
    dob = updated_data.get('dob')
    amount_due = updated_data.get('amount_due')

    cursor.execute("UPDATE student SET first_name = ?, last_name = ?, dob = ?, amount_due = ? WHERE student_id = ?",
                   (first_name, last_name, dob, amount_due, student_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(message='Student updated successfully')

if __name__ == '__main__':
    app.run(debug=True)