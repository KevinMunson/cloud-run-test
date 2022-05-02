import os
from flask import Flask, jsonify, request, Response
import cloudpickle as pickle
import requests
import sys

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

# Route 1 the length teller
@app.route('/predict', methods=[ 'POST'])
def predict(urls):
    #this is loading the model
    clf = pickle.loads('phish-model-1649995335.cloudpickle')
    #now to process the urls to remove protocols
    newurl=[]
    poggers = []
    #these remove the protocls
    for url in urls:
        newurl.append(url.replace('https://',''))

    for url in newurl:
        poggers.append(url.replace('ftp://',''))
    #now to add a / if there is not one in the urls
    #poggers contains the processed urls
    final = []
    fullstring = 'westmountdayschool.org'
    substring = '/'

    for url in poggers:
        if substring not in url:
            url = url+'/'
            final.append(url)
        else:
            final.append(url)
    #we now have final list of processed urls
    #this is where I left off




def url_processor(data):
    '''
    Expects a pandas dataframe with column 'domain', where the domain actually is a full url. (The
    source dataset calls it `domain`.)

    Returns a new dataframe with features extracted from the url.
    '''

    # extract the domain as being everything before the first `/`
    domain = data['domain'].str.split('/').str[0]

    # Add another column called "path" for everything after the first "/", but before any query string (before any `?`, if any)
    #
    # * Hint: There might be multiple `/` in the path, so you can't just modify the code above to take `.str[1]`.
    #   To deal with this, see `n` argument here: https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html
    # * Replace all null-values in with an empty string.
    #   See https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html
    path = pd.Series(data['domain'][0].split('/'))
    path = path.fillna(value='')
    # DataFrame constructor accepts a dict of column-names mapped to pandas series.
    return pd.DataFrame(
        {'domain': domain, 'path': path}
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
