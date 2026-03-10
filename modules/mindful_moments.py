import json

def get_mindfulness_exercise():

    with open("data/mindfulness_prompts.json") as f:
        prompts = json.load(f)

    import random

    return random.choice(prompts)
