from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host='fintech-db',
        user='root',
        password='example',
        database='fintech'
    )

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (%s)', (data['name'],))
    conn.commit()
    conn.close()
    return '', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)