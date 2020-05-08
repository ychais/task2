from flask import Flask, render_template, send_static_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
 

@app.route('/static/<path:path>')
def index2(path):
    return app.send_static_file(path)

 
if __name__ =="__main__":
    app.run(host='localhost', port=5000, debug=True)
