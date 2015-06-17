from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def hello():
    if 'key' in session:
        print(session['key'])
    session['key'] = 'val'
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)

