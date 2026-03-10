from utils.response_templates import positive_responses, negative_responses

def generate_response(text, sentiment):

    label = sentiment["label"]

    if label == "POSITIVE":
        return positive_responses()
    else:
        return negative_responses()
