from flask import Flask, render_template
import random

app = Flask(__name__)

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
    app.run(debug=True)
