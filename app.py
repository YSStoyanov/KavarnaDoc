from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Your application is running successfully!"
