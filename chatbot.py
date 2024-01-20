import nltk
from nltk.chat.util import Chat,reflections

patterns = [
    # Greetings
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you today?"]),
    
    # General inquiries
    (r"how are you", ["I am just a computer program, but I'm doing well. How about you?"]),
    (r"(.*) your name", ["'I'm a chatbot."]),
    
    # Study-related conversation
    (r"tell me about studies", ["Sure, what specific information are you looking for in your studies?"]),
    (r"(.*) study abroad", ["Studying abroad can be a fantastic experience. Are you considering studying abroad?"]),
    (r"(.*) favorite subject", ["I don’t have personal preferences, but I can help you with any subject. What's your favorite subject?"]),
    
    # Farewell
    (r"bye|goodbye", ["Goodbye! If you have more questions, feel free to ask."]),
    
    # Default response
    (r'.*', ["I'm not sure I understand. Can you please rephrase or ask a different question?"]),
]

chatbot=Chat(patterns,reflections)
while True:
    user=input("You:")

    if user.lower()=="exit":
        print("Have a nice day..See u later")
        break
    response=chatbot.respond(user)
    print("Bot:",response)
