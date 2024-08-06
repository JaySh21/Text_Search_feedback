import unittest
from src.search import vectorize_documents, find_most_relevant_doc

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.docs = [
            '''About us. We deliver Artificial Intelligence & Machine Learning solutions to solve business challenges.''',
            '''Contact information. Email [martin davtyan at filament dot ai] if you have any questions.''',
            '''Filament Chat. A framework for building and maintaining a scalable chatbot capability''',
        ]
        self.vectorizer = vectorize_documents(self.docs)

    def test_find_most_relevant_doc(self):
        query = 'contact email to chat to martin'
        most_relevant_doc, similarity = find_most_relevant_doc(self.vectorizer, self.docs, query)
        self.assertEqual(most_relevant_doc, self.docs[1])

if __name__ == '__main__':
    unittest.main()
