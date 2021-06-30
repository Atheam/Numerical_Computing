import pickle

def save_obj(obj,name):
    with open(name+".pkl","wb") as f:
        pickle.dump(obj,f)

def load_obj(name):
    with open(name+".pkl","rb") as f:
        return pickle.load(f)

def articles_info(articles,path):
    articles_info = []
    for article in articles:
        with open(path+article,"r") as f:
            #first line is supposed to be the title
            title = f.readline()
            #second line is supposed to be the link to an original article source
            first_line = f.readline()
            link = None
            if first_line[0] == '#':
                link = first_line[1:]
                first_line = f.readline()
            articles_info.append({"title":title,"link":link,"paragraph":first_line})
    return articles_info
                