# from flask import Flask, render_template,request,jsonify
# from nltk.sentiment import SentimentIntensityAnalyzer
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# import matplotlib.pyplot as plt

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('vader_lexicon')

# app = Flask(__name__)


# def get_sentiment(text):
#     sid = SentimentIntensityAnalyzer()
#     sentiment_score = sid.polarity_scores(text)['compound']
#     return sentiment_score



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat')
# def chat():
#     return render_template('chat.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/r.html')
# def r():
#     return render_template('r.html')

# @app.route('/r1.html')
# def r1():
#     return render_template('r1.html')


# @app.route('/process_entry', methods=['POST'])
# def process_entry():
#     data = request.get_json()
#     entry = data.get('entry', '')
#     date = data.get('calendar','')
#     print("-----------------------------------------------------------------")
#     print(date)
#     words = word_tokenize(entry)
#     filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words('english')]

#         # Calculate sentiment score
#     processed_text = ' '.join(filtered_words)
#     sentiment_score = get_sentiment(processed_text)

#     # Now you have the sentiment_score variable
#     print("Sentiment Score:", sentiment_score)

#     # You can redirect or render another template based on the sentiment_score
#     # For example, redirect to a result page
#     return jsonify({'sentiment_score': sentiment_score})




# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize lists to store dates, sentiment scores, and entries
dates = []
sentiment_scores = []
entries = []

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']
    return sentiment_score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/r.html')
def r():
    return render_template('r.html')

@app.route('/r1.html')
def r1():
    return render_template('r1.html')

@app.route('/process_entry', methods=['POST'])
def process_entry():
    data = request.get_json()
    entry = data.get('entry', '')
    date = data.get('calendar', '')
    print("-----------------------------------------------------------------")
    print("Date:", date)

    words = word_tokenize(entry)
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words('english')]

    # Calculate sentiment score
    processed_text = ' '.join(filtered_words)
    sentiment_score = get_sentiment(processed_text)

    # Store date, sentiment score, and entry in separate lists
    dates.append(date)
    sentiment_scores.append(sentiment_score)
    entries.append({'date': date, 'sentiment_score': sentiment_score})
    print(dates,sentiment_scores)
    # You can redirect or render another template based on the sentiment_score
    # For example, redirect to a result page
    # return jsonify({'sentiment_score': sentiment_score})
    return jsonify({'sentiment_score': sentiment_score, 'dates': dates, 'sentiment_scores': sentiment_scores})


# @app.route('/get_entries', methods=['GET'])
# def get_entries():
#     # Return the entries list as JSON
#     return jsonify(entries)

# @app.route('/get_dates', methods=['GET'])
# def get_dates():
#     # Return the dates list as JSON
#     return jsonify(dates)

# @app.route('/get_sentiment_scores', methods=['GET'])
# def get_sentiment_scores():
#     # Return the sentiment_scores list as JSON
#     return jsonify(sentiment_scores)


@app.route('/get_plot', methods=['GET'])
def get_plot():
    # Generate a sample plot (replace this with your actual data)
    x = dates
    y = sentiment_scores

    # Create the plot
    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Analysis over Time')

    # Save the plot to a BytesIO object
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    plt.close()

    # Convert the image to base64 for embedding in HTML
    img_str = base64.b64encode(img_buf.read()).decode('utf-8')

    # Return the base64 encoded image string
    return jsonify({'plot': img_str})


if __name__ == '__main__':
    app.run(debug=True)
