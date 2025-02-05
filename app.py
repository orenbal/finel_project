from flask import Flask, render_template
import random
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from dotenv import load_dotenv
import os

# טוען משתנים מקובץ .env
load_dotenv()

# משתמש במשתנים מה-.env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


app = Flask(__name__)  # הגדרת Flask פעם אחת בלבד

# חיבור למסד הנתונים
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mypassword@localhost:3307/mydatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # שמירת חיבור למסד הנתונים

# רשימת GIF של חתולים
cat_gifs = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
    "https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif",
    "https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif"
]

@app.route("/")
def index():
    gif_url = random.choice(cat_gifs)  # בחירת GIF רנדומלי
    return render_template("index.html", gif_url=gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)