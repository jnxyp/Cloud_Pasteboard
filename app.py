import random
import string

from flask import Flask, request, abort

max_texts = 1000
max_content_length = 10000
key_length = 6
texts = {}

app = Flask(__name__)


def random_string(length: int = key_length) -> str:
    return ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


@app.route('/status')
def status():  # put application's code here
    return 'Good!'


@app.route('/pasteboard', methods=['POST', 'GET'])
@app.route('/p', methods=['POST', 'GET'])
def pasteboard():
    global texts
    overflow = len(texts) - max_texts
    if len(texts) > max_texts:
        texts = texts[overflow:]

    if request.method == 'POST':
        text = request.form['text']

        if len(text) > max_content_length:
            abort(413)

        key = random_string()
        while key in texts:
            key = random_string()
        texts[key] = text
        return key

    elif request.method == 'GET':
        key = request.args.get('k', '')
        if key not in texts:
            abort(404)
        else:
            return texts[key]


if __name__ == '__main__':
    app.run()
