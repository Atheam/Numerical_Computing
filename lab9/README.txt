###########################################

Aby uruchomic wyszukiwarke nalezy wykonać plik app.py

> python3 app.py


Serwer zostaje odaplony pod adresem localhost:8080/search


###########################################

W przypadku braku artykułów w folderze articles należy je dostarczyć
lub użyć crawlera, uruchamiamy go wykonując

> python3 crawler.py 

nastepnie podac temat (musi być to dokladny temat artykulu ze strony www.nature.com np. computer-science, genetics) oraz ilosc artkułow


###########################################

W przypadku zmiany jakiegos parametru (artykuły, processing IDF, parametr k w svd) lub braku zapisanej macierzy lub slownika termow w folderze pickled
nalezy dokonać obliczenia macierzy ponownie zapisujac ja do pliku, mozna to zrobic wykonujac

>python3 

>>>import engine

>>>engine.recalc() #operacja moze zajac troche czasu (1-5min)


###########################################
