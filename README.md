# finel_project
### **🐱 Flask Cat GIFs - README**
📌 פרויקט Flask שמציג GIF אקראי של חתולים ומחובר למסד נתונים MySQL באמצעות Docker.

---

## **📌 התקנת והפעלת הפרויקט**
### **1️⃣ דרישות מקדימות**
📌 ודאי שהמערכת שלך מכילה את הרכיבים הבאים:
- [Docker](https://www.docker.com/get-started) ו- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.9+
- **VS Code או עורך קוד אחר**

---

### **2️⃣ שיבוט והרצת הפרויקט**
📌 **שכפול הריפו (אם יש גיט)**
```bash
git clone https://github.com/your-repo/cat-gifs-flask.git
cd cat-gifs-flask
```

📌 **בניית והפעלת Docker Compose**
```bash
docker-compose up -d --build
```
🔹 **`-d`** מפעיל את הקונטיינרים ברקע  
🔹 **`--build`** מבצע בנייה מחדש של התמונות  

📌 **בדיקת קונטיינרים פעילים**
```bash
docker ps
```

📌 **בדיקת הלוגים של Flask**
```bash
docker logs finel_project-web-1
```

📌 **בדיקת הלוגים של MySQL**
```bash
docker logs finel_project-db-1
```

📌 **בדיקת חיבור למסד הנתונים**
```bash
docker exec -it finel_project-db-1 mysql -u root -p
```
(הקלידי את הסיסמה `root` כשמתבקשת).

---

### **3️⃣ גישה לאפליקציה**
📌 לאחר שהקונטיינרים עלו, היכנסי לדפדפן ופתחי:
```
http://localhost:5000
```
🔹 אמור להופיע GIF רנדומלי של חתולים 🐱  

---

## **📌 מבנה הפרויקט**
📂 **finel_project/**  
├── 📂 `templates/` → קבצי HTML  
│ ├── `index.html` → תבנית להצגת ה-GIF  
├── 📄 `app.py` → הקובץ הראשי של Flask  
├── 📄 `requirements.txt` → חבילות Python לפרויקט  
├── 📄 `Dockerfile` → בניית הקונטיינר של Flask  
├── 📄 `docker-compose.yaml` → ניהול קונטיינרים  
├── 📄 `init.sql` → סקריפט אתחול מסד נתונים  

---

## **📌 קבצים חשובים**
### **1️⃣ `app.py` (קובץ Flask)**
```python
from flask import Flask, render_template
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# חיבור למסד הנתונים
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db:3306/cat_gifs"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

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
    gif_url = random.choice(cat_gifs)
    return render_template("index.html", gif_url=gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

---

### **2️⃣ `docker-compose.yaml`**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    env_file:
      - .env

  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: cat_gifs
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      MYSQL_ROOT_HOST: "%"
    ports:
      - "3307:3306"
    volumes:
      - db_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  db_data:
```

---

### **📌 3️⃣ `requirements.txt`**
```txt
flask
flask-sqlalchemy
mysql-connector-python
```

---

## **📌 ניהול בסיס הנתונים**
📌 **כניסה למסד הנתונים מתוך Docker:**
```bash
docker exec -it finel_project-db-1 mysql -u root -p
```
📌 **צפייה בטבלאות הקיימות:**
```sql
SHOW DATABASES;
USE cat_gifs;
SHOW TABLES;
```

---

## **📌 פתרון בעיות**
🔹 **אם יש בעיה עם הקונטיינרים, נסי להריץ מחדש:**
```bash
docker-compose down
docker-compose up -d --build
```

🔹 **אם Flask לא עובד, בדקי את הלוגים עם:**
```bash
docker logs finel_project-web-1
```

🔹 **אם MySQL לא עובד, בדקי את החיבור למסד הנתונים:**
```bash
docker exec -it finel_project-db-1 mysql -u root -p
```

---

## **🎉 סיכום**
✅ **הפעלת הפרויקט עם `docker-compose up -d --build`**  
✅ **התחברות ל-MySQL דרך `docker exec -it finel_project-db-1 mysql -u root -p`**  
✅ **גישה לאתר דרך `http://localhost:5000`**  

🚀 **תודה שהשתמשת ב-Flask Cat GIFs!** 🐱🎥  

