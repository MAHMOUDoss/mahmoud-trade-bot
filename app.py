from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ تطبيق محمود شغال الآن على Heroku!"

if __name__ == "__main__":
    app.run()
