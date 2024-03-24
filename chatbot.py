import nltk
from nltk.chat.util import Chat, reflections

# Define reflections for pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define chat patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello User, how can I assist you?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. Your Friend. How can I help you?",]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you for asking!",]
    ],
    [
        r"(.*) your name ?",
        ["My name is Chatbot. Your Friend. How can I help you?",]
    ],
    [
        r"what can you do for me ?",
        ["I can do your tasks. What do you want to ask?!",]
    ],
    [
        r"quit",
        ["Good Bye, Have a great day!",]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Please say again?",]
    ]
]

# Create Chatbot
def chatbot():
    print("Hello! I'm Chatbot.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function
if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
