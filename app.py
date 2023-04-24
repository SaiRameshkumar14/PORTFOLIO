from flask import Flask, render_template

app = Flask(__name__, template_folder="template")


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/skills')
def about():
    return render_template("skills.html")

@app.route('/profile')
def about():
    return render_template("profile.html")

@app.route('/experience')
def about():
    return render_template("Experience.html")

if __name__ == "__main__":
    app.run(debug=True)
