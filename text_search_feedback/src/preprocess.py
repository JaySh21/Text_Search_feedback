import string
from nltk.tokenize import TreebankWordTokenizer

REMOVE_PUNCTUATION_TABLE = str.maketrans({x: None for x in string.punctuation})
TOKENIZER = TreebankWordTokenizer()

def tokenize_and_stem(s):
    return [t.lower() for t in TOKENIZER.tokenize(s.translate(REMOVE_PUNCTUATION_TABLE))]
