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

    # REMOVING PUNCTUATIONS, NUMBERS, & TYPOS
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


    # VARIABLES FOR FUNCTIONS
    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_count = get_word_count(speech_edit_no_stop)
    scores_for_sentences = score_sentences(speech, word_count, max_words)

    # LIST / SUMMARY OF SENTENCE SCORES
    counts = Counter(scores_for_sentences)
    summary = counts.most_common(int(number_of_sentences))
    print('n\SUMMARY:')
    for i in summary:
        print(i[0])

    # REMOVE STOP WORDS FUNCTION
        # return in string
    def remove_stop_words(speech_edit):
        stop_words = set(stopwords.words('english'))
        speech_edit_no_stop = ''
        for word in nltk.word_tokenize(speech_edit):
            if word.lower() not in stop_words:
                speech_edit_no_stop += word + ''
        return speech_edit_no_stop

    # CALCULATING FREQUENCY OF OCCURENCE OF WORDS
    def get_word_freq(speech_edit_no_stop):
        # return a dictionary of word frequency in a string
        word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
        return word_freq

    # SCORING SENTENCES
    def score_sentences(speech, word_freq, max_words):
        sent_scores







