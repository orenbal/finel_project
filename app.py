from flask import Flask, render_template_string
import random

app = Flask(__name__)

# רשימת URL של GIF-ים מוגדרת מראש
gif_urls = [
    "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
    "https://media.giphy.com/media/l4JyK6uFP8E9GdXFe/giphy.gif",
    "https://media.giphy.com/media/Q6joonERc75H2/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif"
]

@app.route('/')
def index():
    # בחירת GIF אקראי מהרשימה
    random_gif = random.choice(gif_urls)
    
    # תבנית HTML מוקצה כטקסט (inline), עם עיצוב בסיסי
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GIF אקראי</title>
        <style>
            body {
                background-color: #f3e5f5;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #4a148c;
                margin-top: 50px;
            }
            img {
                margin: 20px auto;
                border: 5px solid #4a148c;
                border-radius: 10px;
                max-width: 80%;
                height: auto;
            }
            .refresh-btn {
                background-color: #4a148c;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 20px;
                cursor: pointer;
                font-size: 16px;
            }
            .refresh-btn:hover {
                background-color: #6a1b9a;
            }
            footer {
                margin-top: 30px;
                color: #4a148c;
            }
        </style>
    </head>
    <body>
        <h1>תיהנו מ-GIF אקראי!</h1>
        <img src="{{ gif_url }}" alt="GIF אקראי">
        <form method="get" action="/">
            <button class="refresh-btn" type="submit">הצג GIF נוסף</button>
        </form>
        <footer>מופעל על ידי Flask ו-GIPHY</footer>
    </body>
    </html>
    """
    
    return render_template_string(html_template, gif_url=random_gif)

if __name__ == "__main__":
    app.run(debug=True)
