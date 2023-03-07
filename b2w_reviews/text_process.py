import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


from b2w_reviews.logs import log

# @log
def clean_text(text):
    '''Make text lowercase, remove links.
    
    ref
    https://www.kaggle.com/code/tanulsingh077/twitter-sentiment-extaction-analysis-eda-and-model
    '''
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('\n', '', text)
    ## removes words containing numbers, may not be interested to prodctud models
    # text = re.sub('\w*\d\w*', '', text)
    return text

@log
def remove_punctuation(text):
    return text.str.translate(str.maketrans('', '', string.punctuation))

@log
def tokenize(text):
    return text.apply(word_tokenize)

@log
def remove_stopwords(text):
    stopwords_pt = stopwords.words('portuguese')
    pat = '|'.join([r'\b{}\b'.format(w) for w in stopwords_pt])
    return text.str.replace(pat, '', regex=True)

@log
def stemming(text):
    ps = PorterStemmer()
    return text.apply(lambda x: " ".join([ps.stem(word) for word in x.split()]))

# @log
# def stemming(text):
#     ps = PorterStemmer()
#     return " ".join([ps.stem(word) for word in text.split()])

@log
def remove_long_words(text):
    ## todo
    return 