from pickle import GET
from utils import articles_info
from flask import Flask,render_template,request
from engine import Engine

app = Flask(__name__)
engine = Engine()

PATH = "./articles/"

@app.route("/search", methods=["GET","POST"])
def search_results():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        query = request.form["query"]
        results = engine.run_query(query)

        results_info = articles_info(results,PATH)
        return render_template("index.html",info = results_info)


if __name__ == "__main__":
    engine.run_engine()
    app.run(port = 8080)
    

