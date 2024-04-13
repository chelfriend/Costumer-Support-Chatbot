pip install chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('Customer Support Bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Define a function to handle user input and generate bot responses
def get_bot_response(user_input):
    return chatbot.get_response(user_input)

# Main loop to interact with the chatbot
print("Customer Support Bot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Customer Support Bot: Goodbye! Have a great day.")
        break
    response = get_bot_response(user_input)
    print("Customer Support Bot:", response)
