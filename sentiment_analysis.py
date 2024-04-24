import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the data
df = pd.read_csv('japan_data.csv')

# Load the positive and negative word lists
with open("positive.txt", "r") as f:
    positive_words = [word.strip() for word in f.readlines()]

with open("negative.txt", "r") as f:
    negative_words = [word.strip() for word in f.readlines()]

# Initialize the SentimentIntensityAnalyzer and stop_word
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))


# Define a function to preprocess text by removing stopwords
def preprocess_text(text_1):
    word_tokens = word_tokenize(text_1)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)


# Define a function to calculate the NLTK Vader sentiment score
def nltk_sentiment_score(text_2):
    return sia.polarity_scores(text_2)["compound"]


# Empty list for sentiments
nltk_values = []
sentiments = []

# Testing on dataframe
for i in range(len(df)):
    text_original = df.iloc[i]['Title'] + df.iloc[i]['Article']
    text = preprocess_text(text_original)

    # Test the NLTK Vader sentiment score on a sample text
    nltk_sentiment_score_value = nltk_sentiment_score(text)
    nltk_values.append(nltk_sentiment_score_value)

    # Classifying
    if nltk_sentiment_score_value >= 0.5:
        sentiments.append('Positive')
    elif nltk_sentiment_score_value < 0:
        sentiments.append('Negative')
    else:
        sentiments.append('Neutral')

df['Sentiments values'] = nltk_values
df['Sentiments'] = sentiments

# csv_name = 'japan_sentiment.csv'
# df.to_csv(csv_name, index=False)
