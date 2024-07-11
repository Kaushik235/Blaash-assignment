
from flask import Flask, request, jsonify
from better_profanity import profanity
from textblob import TextBlob
from spellchecker import SpellChecker


app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    statement = data.get("statement", "")
   
    detected_profane_words=[]
    for word in statement.split():
        if(profanity.contains_profanity(word)):
            detected_profane_words.append(word)
    
    spell = SpellChecker()
    misspelled_words = spell.unknown(statement.split())
    
    # Extract nouns and sort by length
    text_blob = TextBlob(statement)
    nouns = text_blob.noun_phrases
    sorted_nouns = sorted(nouns, key=len)
    
    return jsonify({
        "misspelled_words": list(misspelled_words),
        "contains_profanity": detected_profane_words,
        "nouns_sorted_by_length": sorted_nouns
    })

if __name__ == "__main__":
    app.run(debug=True, port=8082)