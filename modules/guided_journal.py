journal_prompts = [
"How are you feeling today?",
"What was the most challenging moment today?",
"What is something positive you experienced today?",
"What thoughts are currently occupying your mind?"
]

def get_prompt():

    import random

    return random.choice(journal_prompts)
