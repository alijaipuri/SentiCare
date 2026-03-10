from modules.empathetic_chat import generate_response
from modules.sentiment_analysis import analyze_sentiment

def process_user_input(text):

    sentiment = analyze_sentiment(text)

    response = generate_response(text, sentiment)

    return {
        "sentiment": sentiment,
        "response": response
    }
