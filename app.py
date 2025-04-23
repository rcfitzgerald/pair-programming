import flask

app= flask.Flask(__name__)

@app.route("/")
def index():
    return render_template("Hello World")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
    