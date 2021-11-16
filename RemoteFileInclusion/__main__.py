import requests
from urllib.parse import unquote_plus
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def rfi():
    args = request.args
    path = args.get('page', '')

    try:
        escaped_path = unquote_plus(path)
        data = requests.get(escaped_path).content.strip().decode('utf-8')
        return render_template('index.html', source=data)
    except Exception as e:
        print(e)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
