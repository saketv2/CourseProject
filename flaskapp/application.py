from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import json
# from match_my_voice import Model

application = Flask(__name__)


def hyper_partisan():
    if request.method == 'POST':
        input = request.form.get('text')
        return '<h1> donny is {} </h1>'.format(input)

    return '''<form method="POST"> 
    parsed_text <input type = "text" name = "text">
    <input type = "submit">
    </form>'''

# @application.route('/website_endpoint', methods = ['POST'])
# def handle_input():
#     print(request.get_data())
#     text = str(request.get_data()).split('=')[1]
#     # user = model(text)
#     return text

# @application.route('/', methods = ['POST', 'GET'])
# def fetch_homepage():
#     return render_template("index.html")


@application.route('/json', methods = ['POST'])
def handle_json():
    # data = request.form

    data = json.loads(request.get_data())
    parsedText = data['parsedText']

    text = handle_url(parsedText)
    # print(text)
    # user = model(text)
    return text

def handle_url(input):
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'title', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

    html = urllib.request.urlopen(input).read()
    return text_from_html(html)

# def model(text):
#     us = Model()
#     user = us.predict(text)
#     return user


if __name__ == '__main__':
    application.run(debug = True, port=8088)