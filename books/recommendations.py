from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from .models import Book
def recommend_books(book_title, no_of_recommendations=5):
    books = Book.objects.all()
    book_titles = [ book.title for book in books]
    descriptions = [ book.description  for book in books]
    
    # Vectorize the description using TF-IDF
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(descriptions)
    
    # Compute Cosine similarity between books
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get index of the input book
    idx = book_titles.index(book_title)
    
    # Get similarity scores for the book
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort books based on the similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get indices of the top recommended books
    book_indices = [i[0] for i in sim_scores[1:no_of_recommendations+1]]
    
    return [books[i] for i in book_indices]
    
    
    