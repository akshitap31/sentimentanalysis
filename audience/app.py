# Import libraries
from flask import Flask, render_template, request, jsonify
import pickle
from dataBase.dbFunction import *

modelFile = 'sentiment_model.pickle'

app = Flask(__name__)

# Take care of page not found
@app.errorhandler(404)
# Use inbuilt function which takes error as parameter
def not_found(e):
    # redirect to home page - we can always show custom page
    return render_template("index.html", title="Tweeter Sentiment Analysis")

@app.route("/")
@app.route("/sentimentAnalysis")
def sentimentAnalysis():
    return render_template("index.html", data="")  
@app.route("/audience")
def audience():
    return render_template("audience.html", data="")
@app.route("/line")
def line():
    return render_template("line.html")
@app.route("/tweetData")
def tweetData():
    return jsonify(tweetsData())

@app.route("/tweetUser")
def tweetUser():
    return jsonify(tweetsUser())


@app.route("/tweetsSource")
def tweetsSource():
    return jsonify(tweetSource())


@app.route("/predictSentiment", methods=['POST', 'GET'])
def predictSentiment():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            text = float(request.form['tweet'])

            # Loading the model file  
            loaded_model = pickle.load(open(modelFile, 'rb'))

            # Predict sentiment
            prediction = loaded_model.predict(text)

            # Print prediction
            print('prediction is', prediction)

            # Show the prediction results in a UI
            return render_template('prediction.html', prediction=prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Error occurred during predicting results'
    else:
        return render_template('index.html')

# #Application set to debug mode - update debug flag = False once testing is done
# def create_app():
#     if __name__ == '__main__':
#         app.run(debug=True)
#     return app
if __name__ == '__main__':
    app.run(debug=True)