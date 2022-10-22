from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
import webbrowser
from threading import Timer

def create_app():
    app = Flask(__name__)
    client = MongoClient(
        "mongodb+srv://dhilipmaharish:dibots97@microblog.chrtjkp.mongodb.net/test")
    app.db = client.micro_blog

    @app.route("/dhilipblog", methods=["GET", "POST"])
    def display():
        if request.method == "POST":
            entry_content = request.form.get("blog_story")
            formated_date = datetime.datetime.today().strftime("%y-%m-%d")
            #entries.append((entry_content, formated_date))
            # print(entries)
            app.db.entities.insert_one(
                {"content": entry_content, "date": formated_date})
            for ele in app.db.entities.find({}):
                print(ele)

        entry_with_date = [(entry["content"], entry["date"], datetime.datetime.strptime(
            entry["date"], "%y-%m-%d").strftime("%b %d '%y")) for entry in app.db.entities.find({})]
        print(entry_with_date)
        return render_template("index.html", entries = entry_with_date)
    
    return app

create_app().run()
# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:5000/')

#create_app().run(port=5987)

# if __name__ == "__main__":
#     # Timer(1, open_browser).start()
#     create_app.run(port=5000)
