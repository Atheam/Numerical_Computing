import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.preprocessing import normalize
from collections import Counter
import string
from os import listdir
import numpy as np
from scipy.sparse.linalg import svds
import utils

PATH = "./articles/"

def preprocess(text):
    
    text = text.lower()
    #removing punctuation
    text = text.translate(str.maketrans('','',string.punctuation))
    #tokenized text
    tokenized = nltk.word_tokenize(text)
    #remove garbage
    filtered_words = [word for word in tokenized if len(word) > 1]
    #filtering stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in filtered_words if word not in stop_words]
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
    matrix = np.zeros((len(terms),len(articles)),dtype=np.float32)
    for bag_idx,bag in enumerate(bags):
        for word in bag:
            matrix[terms[word],bag_idx] = bag[word]
    return matrix

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

def recalc(IDF = True,svd = True):
    terms, bags = create_terms(PATH)
    if IDF:
        process_IDF(bags)
    A = create_matrix(PATH,terms,bags)
    if svd:
        A = low_rank_approx(A,200)
        
    utils.save_obj(A,"./pickled/matrix_file")
    utils.save_obj(terms,"./pickled/terms_file")

class Engine():

    def run_engine(self):
        self.A = normalize(utils.load_obj("./pickled/matrix_file"),axis=0)
        self.terms = utils.load_obj("./pickled/terms_file")
    
    def search(self,path,q,A):
        articles = listdir(path)
        q = normalize(q.reshape(-1,1))
        return np.dot(q.T,A)

    def create_q_vector(self,query,terms):
        processed = preprocess(query)
        bag = Counter(processed)
        q = np.zeros(len(terms),dtype=np.float32)
        for word in bag:
            if word in terms:
                q[terms[word]] = bag[word]
        return q

    def run_query(self,query):
        
        q = self.create_q_vector(query,self.terms)
        articles = listdir(PATH)
        results = []
        coefs = self.search(PATH,q,self.A)

        for i in np.argsort(coefs)[0][-10:][::-1]:
            #print(coefs[0][i])
            results.append(articles[i])

        return results


