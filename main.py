from flask import Flask, send_from_directory, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/images/<path:filename>')
def index1 (filename):
    return send_from_directory('images', filename)

@app.route('/static/css/<path:filename>')
def index2 (filename):
    return send_from_directory('css', filename)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
