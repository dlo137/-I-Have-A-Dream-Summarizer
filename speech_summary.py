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

    # SCAN AND JOIN PARAGRAPH ELEMENTS
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elements = soup.select('p')
    speech = ''.join(p_elements)

    # REMOVE PUNCTUATIONS, NUMBERS, & TYPOS
    speech = speech.replace(')mowing', 'knowing')
    speech = re.sub('\s+', '', speech)
    speech_edit = re.sub('[^a-zA-Z','', speech)
    speech_edit = re.sub('\s+', '', speech_edit)

    # LOGIC FOR USER'S INPUT REQUIRMENTS
    while True:
        max_words = input('Enter max words per sentence for summary: ')
        number_of_sentences = input('Enter number of sentences for summary')

        if max_words.isdigit() and number_of_sentences.isdigit():
            break
        else:
            print('\nInput must be in whole numbers\n')

    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)
    sent_scores = score_sentences(speech, word_freq, max_words)

    
