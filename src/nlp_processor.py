
from transformers import pipeline

class NLPProcessor:
    def __init__(self):

        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
        self.sentiment_analyzer = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis", device=-1)

    def summarize_text(self, text):
        summary = self.summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def analyze_sentiment(self, text):
        sentiment = self.sentiment_analyzer(text)
        return sentiment[0]['label']
