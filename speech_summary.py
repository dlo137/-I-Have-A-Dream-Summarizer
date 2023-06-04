from collections import Counter
import re
import requests
import bs4
import nltk
from nltk.corpus import stopwords

def main():
    # GRABBING SPEECH FROM URL
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()

    #FIND AND JOIN PARAGRAPH TEXTS
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elements = soup.select('p')
    speech = ''.join(p_elements)

    #REMOVE PUNCTUATION, NUMBERS, & TYPOS
    speech = speech.replace(')mowing', 'knowing')
    speech = re.sub('\s+', '', speech)
    speech_edit = re.sub('[^a-zA-Z','', speech)
    speech_edit = re.sub('\s+', '', speech_edit)