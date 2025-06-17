from flask import Flask,send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def default_func():
    return send_from_directory('portfolio', 'index.html')

@app.route('/components')
def components():
    return send_from_directory('portfolio', 'components.html')


@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join('portfolio', 'assets'), filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')