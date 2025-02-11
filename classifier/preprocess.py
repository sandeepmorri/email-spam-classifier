import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string
from string import punctuation
from nltk.stem.porter import PorterStemmer
nltk.download('punkt_tab')
ps = PorterStemmer()
def preprocess_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)