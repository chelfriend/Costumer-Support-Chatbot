pip install chatterbot
# chatbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
chatbot = ChatBot('SupportBot')

# Define a function to train the chatbot on domain-specific data
def train_chatbot(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        conversation_data = file.readlines()
    trainer = ListTrainer(chatbot)
    trainer.train(conversation_data)

# Train the chatbot on domain-specific data
train_chatbot('data.csv')

# Define a function to handle user input and generate bot responses
def get_bot_response(user_input):
    return chatbot.get_response(user_input)

# Main loop to interact with the chatbot
print("SupportBot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("SupportBot: Goodbye! Have a great day.")
        break
    response = get_bot_response(user_input)
    print("SupportBot:", response)
