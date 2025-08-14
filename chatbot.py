import re
import random

# A list of patterns and corresponding responses.
# The `r"..."` prefix indicates a raw string, which is good for regex.
# The `(.*)` is a regex group that captures the text it matches.
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there!", "Hey! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["You can call me CustomerBot.", "I am CustomerBot, your virtual assistant."]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you for asking!", "I'm a bot, but I'm functioning perfectly!"]
    ],
    [
        r"store hours|when are you open",
        ["Our store is open from 9 AM to 5 PM, Monday to Friday.", "We operate from 9 to 5 on weekdays."]
    ],
    [
        r"return policy",
        ["You can return any item within 30 days of purchase with a valid receipt.", "Our return policy allows for returns in 30 days."]
    ],
    [
        r"where is my order|order status",
        ["Please provide your order number, and I can check the status for you.", "I can track your order. What's the order number?"]
    ],
    [
        r"bye|goodbye|exit",
        ["Goodbye! Have a great day.", "It was nice chatting with you. Feel free to come back anytime!"]
    ],
    [
        r"(.*)", # This is a fallback pattern for any unhandled input.
        ["I'm sorry, I don't understand that. Could you please rephrase?", "I'm not sure how to respond. Can you ask a different question?"]
    ]
]

def get_response(user_input):
    """
    Takes user input and returns a suitable response based on the defined rules.
    """
    user_input = user_input.lower()
    for pattern, responses in pairs:
        match = re.search(pattern, user_input)
        if match:
            return random.choice(responses)
    return "I'm having trouble understanding you. Could you try a different question?"

def chat():
    """
    The main function to run the chatbot.
    """
    print("🤖 Hello! I am CustomerBot. How can I help you today? Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye", "goodbye"]:
            print("CustomerBot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print(f"CustomerBot: {response}")

if __name__ == "__main__":
    chat()