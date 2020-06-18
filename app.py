from flask import Flask, render_template, flash, redirect, request, url_for
from src import graphsearch, setupgraph
import time
from os import path

app = Flask(__name__)
app.secret_key = "dummysecret"

APP_PATH = app.root_path
dataSetFilename = path.join(APP_PATH, "data/wikipediaMoviesDataDump.json")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/bacon_path', methods=['POST'])
def getBaconPath():
    if request.method == 'POST':
        fromActor = request.form['fromActor'].title()
        toActor = request.form['toActor'].title()

        graph = setupgraph.setupGraph(dataSetFilename)

        start = time.time()
        baconPath = graphsearch.bfs(graph, fromActor, toActor)
        end = time.time()

        searchTime = round(end - start, 3)

        if baconPath:
            flash(u'Found Connection! ' + baconPath, '200')
            flash(u'Searched in ' + str(searchTime) + ' seconds', '200')
        else:
            flash('No connection found between ' + fromActor + ' and ' + toActor, '404')
            flash(u'Searched in ' + str(searchTime) + ' seconds', '200')
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
