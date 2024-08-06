from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocess.py import tokenize_and_stem

def vectorize_documents(docs):
    vectorizer = TfidfVectorizer(tokenizer=tokenize_and_stem, stop_words='english')
    vectorizer.fit(docs)
    return vectorizer

def find_most_relevant_doc(vectorizer, docs, query):
    query_vector = vectorizer.transform([query]).todense()
    doc_vectors = vectorizer.transform(docs)
    similarity = cosine_similarity(query_vector, doc_vectors)
    ranks = (-similarity).argsort(axis=None)
    return docs[ranks[0]], similarity
