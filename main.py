from flask import Flask, render_template
import nlp as nlp

app = Flask(__name__)

@app.route("/") 
def hello_world():
    return render_template('layout.html')

@app.route("/home") 
def home():
    return render_template('home.html') 

@app.route("/submit")
def form():
    # str = '/Users/muhammadhamzasohail/Desktop/Tester_ALDA'
    # str1 = '/Users/muhammadhamzasohail/Desktop/Summary_files'
    # result = nlp.path_adder(str)
    # nlp.batch_processor(result, str, str1)
    return render_template('form.html')


@app.route("/last")
def last():
    # str = '/Users/muhammadhamzasohail/Desktop/Tester_ALDA'
    # str1 = '/Users/muhammadhamzasohail/Desktop/Summary_files'
    # result = nlp.path_adder(str)
    # nlp.batch_processor(result, str, str1)
    return render_template('last.html')

if __name__ == "__main__":
    app.run   