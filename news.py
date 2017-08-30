from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os
import markdown

app = Flask(__name__)
CORS(app)

@app.route("/news/")
def index():
        news_files = os.listdir("news_files")
        news_files.sort()
        news_files = list(reversed(news_files))
        news_items = []
        for i in range(len(news_files)):
                news_file = news_files[i]
                file = open("news_files/" + news_file, "r")
                html = markdown.markdown(file.read())
                news_items.append({"html": html})
                file.close()
        return json.dumps(news_items)
