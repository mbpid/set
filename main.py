from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/programa.html")
def programa():
    return render_template("programa.html")

@app.route("/disciplina.html")
def disciplina():
    return render_template("disciplina.html")

@app.route("/moodle")
def moodle():
    return render_template("moodle.html")

if __name__ == "__main__":
    app.run(debug=True)