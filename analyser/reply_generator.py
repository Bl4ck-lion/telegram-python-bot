from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Quotes Bot',read_only = True, logic_adapters=[
        "chatterbot.logic.BestMatch"
    ])

# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")

def get_response(message):
    message = message.lower()
    return chatbot.get_response(message)
