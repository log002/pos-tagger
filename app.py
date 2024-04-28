from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

# Load the Spacy model
nlp = spacy.load("en_core_web_lg")

# Define a function that processes the input text with Spacy
def process_input(docs):
    txt = nlp(docs)
    result = []
    for token in txt:
        if token.pos_ not in ["SPACE", "X", "PUNCT"]:
            result.append((token.text, spacy.explain(token.pos_), spacy.explain(token.tag_)))
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    docs = request.form['text']
    processed_result = process_input(docs)
    print("Processed Result:", processed_result)  # Add this line for debugging
    return render_template("index.html", d=docs, processed_result=processed_result)

if __name__ == '__main__':
    app.run(debug=True)
