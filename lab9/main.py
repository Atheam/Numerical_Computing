import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.preprocessing import normalize
from collections import Counter
import string
from os import listdir
import numpy as np
from numpy.linalg import norm
from scipy.sparse.linalg import svds

PATH = "./articles/"

def preprocess(text):
    
    text = text.lower()
    #removing punctuation
    text = text.translate(str.maketrans('','',string.punctuation))
    #tokenized text
    tokenized = nltk.word_tokenize(text)

    #filtering stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in tokenized if word not in stop_words]

    #stemming words
    ps = PorterStemmer()
    stemmed = [ps.stem(word) for word in filtered_words]
    
    return stemmed
        
def create_terms(path):
    terms = {}
    articles = listdir(path)
    term_idx = 0
    bags = []
    for filename in articles:
        with open(path+filename,"r") as f:
            words = preprocess(f.read())
            bags.append(Counter(words))
            for word in words:
                if word not in terms:
                    terms[word] = term_idx
                    term_idx+=1
    return terms,bags

def create_matrix(path,terms,bags):
    articles = listdir(path)

    matrix = np.zeros((len(terms),len(articles)))

    for bag_idx,bag in enumerate(bags):
        for word in bag:
            matrix[terms[word]][bag_idx] = bag[word]
    
    return matrix

def create_q_vector(query,terms):
    processed = preprocess(query)
    bag = Counter(processed)
    q = np.zeros(len(terms))
    for word in bag:
        if word in terms:
            q[terms[word]] = bag[word]
    return q
    
def search(path,q,A):
    articles = listdir(path)
    q = normalize(q.reshape(-1,1))
    A = normalize(A,axis = 0)
    return q.T@A

def process_IDF(bags):
    words = [word for bag in bags for word in bag]
    occurences = Counter(words)
    N = len(bags)
    for bag in bags:
        for word in bag:
            bag[word] *= np.log(N/occurences[word])


def low_rank_approx(A,k):
    U,S,V = svds(A,k=k)
    A_approx = U @ np.diag(S) @ V
    return A_approx


def run(svd = True,IDF = True):

    def show_titles(articles):
        for article in articles:
            with open("./articles/"+article,"r") as f:
                print(f.readline())

    terms, bags = create_terms(PATH)
    if IDF:
        process_IDF(bags)
    A = create_matrix(PATH,terms,bags)
    if svd:
        A = low_rank_approx(A,200)

    while(1):
        query = input("Wprowadz query: ")
        q = create_q_vector(query,terms)
        articles = listdir(PATH)
        results = []
        for i in np.argsort(search(PATH,q,A))[0][-4:][::-1]:
            results.append(articles[i])
        show_titles(results)

run()

