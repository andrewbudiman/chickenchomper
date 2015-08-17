from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/miniprojects")
def miniprojects():
    return render_template('miniprojects.html')

@app.route("/dotfiles")
def dotfiles():
    return render_template('dotfiles.html')

@app.route("/games")
def games():
    return render_template('games.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
