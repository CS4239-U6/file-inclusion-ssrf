import os
from flask import Flask, abort, render_template, request

app = Flask(__name__)
ROOT_FILE = os.path.join(os.path.dirname(__file__), 'files')


@app.route('/')
def lfi():
    args = request.args
    path = args.get('page', '')

    if (len(path) == 0):
        return render_template('index.html')

    file_path = os.path.join(ROOT_FILE, path)
    if not os.path.isfile(file_path):
        return abort(404)
    with open(file_path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
