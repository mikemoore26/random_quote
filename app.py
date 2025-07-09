from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Discipline equals freedom. – Jocko Willink",
    "Whether you think you can or you can't, you're right. – Henry Ford",
    "Do or do not. There is no try. – Yoda",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "Success is not final, failure is not fatal. It is the courage to continue that counts. – Winston Churchill"
]

@app.route("/quotes")
def get_quotes():
    return jsonify({"quotes": quotes})

@app.route("/quotes/random")
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({"quote": random_quote})


if __name__ == "__main__":
    app.run(debug=True)