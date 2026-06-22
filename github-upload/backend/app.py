from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = os.environ.get('REDIS_PORT', '6379')
redis_password = os.environ.get('REDIS_PASSWORD', '')

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "message": "pong"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "name": "许愿",
        "student_id": "202321001",
        "message": "Hello from Flask Backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)