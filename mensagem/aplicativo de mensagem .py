#biblioteca Flask

#pip install Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json['content']
    messages.append(content)
    return jsonify({'status': 'success'})

@app.route('/message', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run()
