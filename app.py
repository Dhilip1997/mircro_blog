from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient("mongodb+srv://dhilip1997:dibots97@blogging.sgsphrd.mongodb.net/?retryWrites=true&w=majority")
# entries =[]
# app.db = client.blogs

@app.route("/", methods=["GET","POST"])
def display():
    if request.method == "POST":
        entry_content = request.form.get("blog_story")
        formated_date = datetime.datetime.today().strftime("%y-%m-%d")
    #     entries.append((entry_content, formated_date))
    #     app.db.entries.insert_one({"content": entry_content, "date": formated_date})

    # entry_with_date = [(entry["content"], entry["date"], datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d '%y")) for entry in app.db.entries.find({})]
    return render_template("index.html")
    
app.run(port= 8080)
