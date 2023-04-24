from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/skills')
def skills():
    return render_template("skills.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/experience')
def experience():
    return render_template("experience.html")


if __name__ == "__main__":
    app.run(debug=True)
