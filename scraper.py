import bs4
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

def handleURL(input):

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