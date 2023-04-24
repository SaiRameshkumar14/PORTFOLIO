from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="template")


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
