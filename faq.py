from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(
    "./data/"
)

# Now let's get a response to a greeting
##response = chatbot.get_response('在？')
##print(response)

lineCounter=1

while True:
    print(chatbot.get_response(input("(" + str(lineCounter) + ") user:")))
    lineCounter += 1
