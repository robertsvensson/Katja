from flask import Flask
from flask import render_template
import markdown

app = Flask(__name__)

@app.route("/")
def hello():
    f = open('markdown.md', 'r')
    markdownFile = f.read()

    stringOfMarkdown = markdown.markdown(markdownFile, extensions=['markdown.extensions.attr_list','markdown.extensions.codehilite','markdown.extensions.fenced_code'])
    return render_template('index.html', stringOfMarkdown = stringOfMarkdown)
