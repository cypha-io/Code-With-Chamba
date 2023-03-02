import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!"]
    ],
    [
        r"what can you do|what are your capabilities",
        ["I can help you with general queries, tell jokes, or play a game with you."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"play a game",
        ["Sure, let's play a guessing game. I'm thinking of a number between 1 and 10. What is it?"]
    ],
    [
        r"([0-9]*)",
        [
            "Sorry, that's incorrect. Try again!",
            "Nope, not quite. Guess again!",
            "Wrong! Keep trying."
        ]
    ],
    [
        r"quit",
        ["Goodbye!"]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
