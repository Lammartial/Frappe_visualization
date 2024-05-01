from flask import Flask
from visualization import visualization

app = Flask(__name__)
@app.route("/")
def main():
    return "<h1>Hello there!</h1>"

app.register_blueprint(visualization)

if __name__ == "__main__":
    app.run(host='0.0.0.0')