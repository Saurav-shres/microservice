from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "A habit cannot be tossed out the window; it must be coaxed down the stairs a step at a time. -Mark Twain",
    "Discipline is choosing between what you want now and what you want most. -Abraham Lincoln",
    "I fear not the man who has practiced 10,000 kicks, but I do fear the man who has practiced one kick 10,000 times. -Bruce Lee",
    "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. -Albert Einstein",
    "Tis easier to prevent bad habits than to break them. - Benjamin Franklin",
    "Success is the sum of small efforts repeated day in and day out. -Robert Collier",
    "Successful people are simply those with successful habits. -Brian Tracy",
    "Motivation is what gets you started. Habit is what keeps you going. - Jim Rohn",
    "Good habits formed at youth make all the difference. - Aristotle",
    "And once you understand that habits can change, you have the freedom and the responsibility to remake them. -Charles Duhigg"
]


@app.route('/quote', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify({"quote": random_quote})


if __name__ == '__main__':
    app.run(debug=True)