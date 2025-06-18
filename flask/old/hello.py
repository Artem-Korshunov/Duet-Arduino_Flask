from flask import Flask
import requests as r

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello, world!"
#if __name__ == "__main__":
app.run()