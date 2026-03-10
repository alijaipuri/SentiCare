import random

positive = [
"I'm glad to hear you're feeling good.",
"That sounds positive. Keep nurturing those feelings.",
"It's great that you're experiencing something uplifting."
]

negative = [
"I'm sorry you're feeling this way.",
"That sounds difficult. Do you want to talk more about it?",
"It's okay to feel this way sometimes."
]

def positive_responses():
    return random.choice(positive)

def negative_responses():
    return random.choice(negative)
